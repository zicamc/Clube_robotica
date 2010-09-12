# -*- coding: utf-8 -*-
import sys
import pygame
import pygame.font
from caixa import caixa
from configuracoes import config_caixa
from configuracoes import config_selecao

pygame.font.init()
fonte = pygame.font.Font("comic.ttf", 25)
#===============================================================================
#                   CAIXA BUZZER
#===============================================================================
class caixa_buzzer(caixa):
    def __init__(self):
        """

        """
        caixa.__init__(self)
        self.imagem = pygame.image.load("Imagens/buzzer.gif").convert()
        self.imagem_selecao = pygame.image.load("Imagens/Caixa_buzzer.gif").convert()

        fonte = pygame.font.Font("comic.ttf", config_selecao.data['caixa_buzzer'][self.lingua]['tamanho'])
        texto = fonte.render(config_selecao.data['caixa_buzzer'][self.lingua]['texto'], True, (0, 0, 0))
        self.imagem_selecao.blit(texto,(15,0))
        self.tempo = 0.0
        self.escreve = "0"
        """

        """

    def show(self, SCREEN, posx):
        """
        Só mostra se houver alguma parte vísivel para o usuário ou seja, se a posição ficar entre -100 e 620
        """
        if (self.posicao[0]-posx < 620 and self.posicao[0]-posx > -160):
            font = pygame.font.Font("comic.ttf", 30)

            self.rect = SCREEN.blit(self.imagem, (self.posicao[0]-posx, self.posicao[1]))

            fonte = pygame.font.Font("comic.ttf", config_caixa.data['caixa_buzzer'][self.lingua]['tamanho'])
            texto = fonte.render(config_caixa.data['caixa_buzzer'][self.lingua]['texto'], True, (0, 0, 0))
            SCREEN.blit(texto, (self.posicao[0]-posx + 50 - texto.get_width()/2 , self.posicao[1]))

            #Texto centralizado do buzzer
            texto = font.render(self.escreve[1:]+"s", True, (0, 0, 0))
            tam_text = texto.get_width()/2

            SCREEN.blit(texto, (self.posicao[0]-posx+50-tam_text , self.posicao[1] + 50))

            pygame.draw.line(SCREEN, (0, 0, 0, 0),
                             (self.posicao[0]-posx + 100, self.posicao[1] + 50),
                             (self.posicao[0]-posx + 125, self.posicao[1] + 50), 15)

            pygame.draw.polygon(SCREEN, (0, 0, 0, 0),
                                ((self.posicao[0]-posx + 125, self.posicao[1] + 25), (self.posicao[0]-posx + 125, self.posicao[1] + 75),
                                (self.posicao[0]-posx + 150, self.posicao[1] + 50)))
            #pygame.display.update((self.posicao[0]-posx,self.posicao[1],300-posx,300))

        else:
            self.rect = 0

    def events(self, SCREEN, posx):
        """

        """
        #BUG - Tempo em décimos só pode aceitar um dígito!
        SCREEN.blit(self.imagem, (self.posicao[0]-posx, self.posicao[1]))
        list_point = ((self.posicao[0]-posx + 24, self.posicao[1] + 189), (self.posicao[0]-posx + 78, self.posicao[1] + 189),
                      (self.posicao[0]-posx + 24, self.posicao[1] + 217), (self.posicao[0]-posx + 78, self.posicao[1] + 217))
        button_ok = pygame.draw.polygon(SCREEN, (0, 0, 0, 0), list_point)
        SCREEN.blit(self.imagem_selecao, (self.posicao[0]-posx-25, self.posicao[1] + 100))

        fonte = pygame.font.Font("comic.ttf", config_caixa.data['caixa_buzzer'][self.lingua]['tamanho'])
        texto = fonte.render(config_caixa.data['caixa_buzzer'][self.lingua]['texto'], True, (0, 0, 0))
        SCREEN.blit(texto, (self.posicao[0]-posx + 50 - texto.get_width()/2 , self.posicao[1]))
        TELA = SCREEN.copy()

        texto = fonte.render(self.escreve[1:], True, (255, 255, 255))
        SCREEN.blit(texto, (self.posicao[0]-posx + 20, self.posicao[1] + 134))
        pygame.display.update((0, 0, 620, 600))

        condicao = False

        while condicao == False:
            self.treat_events()
            self.CLOCK.tick(10)
            for event in pygame.event.get((pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN)):

                if event.type == pygame.KEYDOWN:
                    key = event.key
                    self.teclado_numerico(key)

                    texto = fonte.render(self.escreve[1:], True, (255, 255, 255))
                    SCREEN.blit(TELA, (0, 0))
                    SCREEN.blit(texto, (self.posicao[0]-posx + 20, self.posicao[1] + 134))
                    pygame.display.update((self.posicao[0]-posx, self.posicao[1] + 134, 100, 100))

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_ok.collidepoint(pygame.mouse.get_pos()):
                        self.tempo = float(self.escreve)
                        if self.tempo != 0.0:
                            self.selecao_visivel = False
                            condicao = True

    def recria(self,pos,tempo):
        self.escreve = tempo
        self.posicao = pos
        self.escreve = '0'+str(tempo)
        self.tempo = float(tempo)


    def gera_texto(self):
        self.prog_text = ""
        self.prog_text += ("04-")
        self.prog_text += str(self.tempo)

    def gera_programa(self):
        self.prog_arduino = chr(4)
        time = int(self.tempo*10)
        print time
        while time > 250:
            self.prog_arduino += chr(250)
            time -= 250
            print time
            self.prog_arduino += chr(4)
        self.prog_arduino += chr(time)