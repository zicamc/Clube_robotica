# -*- coding: utf-8 -*-
import sys
import pygame
import pygame.font
from caixa import caixa
from configuracoes import config_caixa
from configuracoes import config_selecao
from configuracoes import all_config

pygame.font.init()
CLOCK = pygame.time.Clock()
fonte = pygame.font.Font("comic.ttf", 25)
#===============================================================================
#                   CAIXA BUZZER
#===============================================================================
class caixa_buzzer(caixa):
    def __init__(self):
        """

        """
        self.imagem = pygame.image.load("Imagens/buzzer.gif").convert()
        self.rect = 0
        self.posicao = (0, 0)
        self.lingua = all_config.data['lingua']

        self.imagem_selecao = pygame.image.load("Imagens/Caixa_buzzer.gif").convert()

        fonte = pygame.font.Font("comic.ttf", config_selecao.data['caixa_buzzer'][self.lingua][0]['tamanho'])
        texto = fonte.render(config_selecao.data['caixa_buzzer'][self.lingua][0]['texto'], True, (0, 0, 0))
        pos = eval(config_selecao.data['caixa_buzzer'][self.lingua][0]['pos'])
        self.imagem_selecao.blit(texto,pos)

        self.selecao_visivel = True
        self.tempo = 0.0
        self.escreve = "0"
        """

        """

    def troca_posicao(self, posicao):
        """

        """
        self.posicao = posicao
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
            pos = eval(config_caixa.data['caixa_buzzer'][self.lingua]['pos'])
            SCREEN.blit(texto, (self.posicao[0]-posx + pos[0], self.posicao[1] + pos[1]))

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
        """

        """

    def events(self, SCREEN, posx):
        """

        """
        #BUG - Tempo em décimos só pode aceitar um dígito!
        SCREEN.blit(self.imagem, (self.posicao[0]-posx, self.posicao[1]))
        list_point = ((self.posicao[0]-posx + 24, self.posicao[1] + 189), (self.posicao[0]-posx + 78, self.posicao[1] + 189),
                      (self.posicao[0]-posx + 24, self.posicao[1] + 217), (self.posicao[0]-posx + 78, self.posicao[1] + 217))
        button_ok = pygame.draw.polygon(SCREEN, (0, 0, 0, 0), list_point)
        SCREEN.blit(self.imagem_selecao, (self.posicao[0]-posx-25, self.posicao[1] + 100))

        TELA = SCREEN.copy()

        texto = fonte.render(self.escreve[1:], True, (255, 255, 255))
        SCREEN.blit(texto, (self.posicao[0]-posx + 20, self.posicao[1] + 134))
        pygame.display.update((0, 0, 620, 600))

        condicao = False

        while condicao == False:
            treat_events()
            CLOCK.tick(10)
            for event in pygame.event.get((pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN)):

                if event.type == pygame.KEYDOWN:
                    key = event.key
                    if self.escreve == "":
                        self.escreve = "0"
                    if (key == pygame.K_PERIOD or key == pygame.K_KP_PERIOD):
                        if self.escreve.find('.') == -1:
                            self.escreve += '.'

                    if int(self.tempo) > 99 or ((self.tempo * 100) % 10 < 10 and ((self.tempo * 100) % 10 > 0)):
                        tamanho = len(self.escreve)
                        self.escreve = self.escreve[0:(tamanho-1)]
                    if key == pygame.K_0 or key == pygame.K_KP0:
                        if self.escreve.count('0') < 2:
                            self.escreve += '0'

                    elif key == pygame.K_1 or key == pygame.K_KP1:
                        self.escreve += '1'
                    elif key == pygame.K_2 or key == pygame.K_KP2:
                        self.escreve += '2'
                    elif key == pygame.K_3 or key == pygame.K_KP3:
                        self.escreve += '3'
                    elif key == pygame.K_4 or key == pygame.K_KP4:
                        self.escreve += '4'
                    elif key == pygame.K_5 or key == pygame.K_KP5:
                        self.escreve += '5'
                    elif key == pygame.K_6 or key == pygame.K_KP6:
                        self.escreve += '6'
                    elif key == pygame.K_7 or key == pygame.K_KP7:
                        self.escreve += '7'
                    elif key == pygame.K_8 or key == pygame.K_KP8:
                        self.escreve += '8'
                    elif key == pygame.K_9 or key == pygame.K_KP9:
                        self.escreve += '9'

                    self.tempo = float(self.escreve)
                    if int(self.tempo) > 99 or ((self.tempo * 100) % 10 < 10 and ((self.tempo * 100) % 10 > 0)):
                        tamanho = len(self.escreve)
                        self.escreve = self.escreve[0:(tamanho-1)]

                    if key == pygame.K_BACKSPACE or key == pygame.K_DELETE:
                        tamanho = len(self.escreve)
                        self.escreve = self.escreve[0:(tamanho-1)]

                    texto = fonte.render(self.escreve[1:], True, (255, 255, 255))
                    SCREEN.blit(TELA, (0, 0))
                    SCREEN.blit(texto, (self.posicao[0]-posx + 20, self.posicao[1] + 134))
                    pygame.display.update((self.posicao[0]-posx, self.posicao[1] + 134, 100, 100))

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_ok.collidepoint(pygame.mouse.get_pos()):
                        self.tempo = float(self.escreve)
                        if self.tempo != 0.0:
                            print "OIUUUGGGG"
                            self.selecao_visivel = False
                            condicao = True

        """

        """

    def colide(self, pos):
        """

        """
        try:
            return self.rect.collidepoint(pos)
        except:
            return 0
        """

        """

    def retorna_pos(self):
        """

        """
        return self.posicao
        """

        """

def treat_events():
    """
    Função que verifica se algo aconteceu para que o programa se feche. Aqui por preguica, nao tava afim de faze um import!
    """
    # Criar uma thread para isso
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                                           sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:     sys.exit()

    """ """
