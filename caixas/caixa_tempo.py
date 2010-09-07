# -*- coding: utf-8 -*-
import pygame
import pygame.font
from caixa import caixa
from configuracoes import config_caixa

pygame.font.init()
fonte = pygame.font.Font("comic.ttf", 25)
#===============================================================================
#                   CAIXA TEMPO
#===============================================================================
class caixa_tempo(caixa):
    def __init__(self):
        """

        """
        caixa.__init__(self)

        self.imagem = pygame.image.load("Imagens/delay.gif").convert()
        self.imagem_selecao = pygame.image.load("Imagens/Caixa_tempo.gif").convert()
        self.selecao_visivel = True
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

            fonte = pygame.font.Font("comic.ttf", config_caixa.data['caixa_tempo'][self.lingua]['tamanho'])
            texto = fonte.render(config_caixa.data['caixa_tempo'][self.lingua]['texto'], True, (0, 0, 0))
            SCREEN.blit(texto, (self.posicao[0]-posx +50 - texto.get_width()/2, self.posicao[1]))

            #Texto do tempo centralizado
            texto = font.render(self.escreve[1:]+"s", True, (0, 0, 0))
            SCREEN.blit(texto, (self.posicao[0]- posx + 50 - texto.get_width()/2 , self.posicao[1] + 50))

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
        Oi
        """

    def events(self, SCREEN, posx):
        """
        Em implementação: Está classe será primária, quando estiver em execução, ou seja, o usuário só sai dela se clicar no okay
        ou deletar a caixa( Vai ser implementado)
        
        1 - Dá o blit da cixa
        2 - Cria uma lista de pontos que são o botao Okay
        3 - Com a lista de pontos faz um draw preto que simbolizará o botão para testar se o mesmo for clicado
        4 - Da um blit da caixa de selecao, sobrepondo o botao do Okay
        5 - Faz um update da tela no local que foi feito os novos blit
        6 - Copia a tela, para quando houver algum blit só ser refeito aquela parte.
        7 - Entra num while condicional que será até que o botão direito for clicado em qualquer parte ou se o botão okay for clicado
        8 - Limitação de execuções por segundo
        9 - 
        """
        #BUG - Tempo em décimos só pode aceitar um dígito!

        SCREEN.blit(self.imagem, (self.posicao[0]-posx, self.posicao[1]))
        list_point = ((self.posicao[0]-posx + 24, self.posicao[1] + 164), (self.posicao[0]-posx + 78, self.posicao[1] + 164),
                      (self.posicao[0]-posx + 24, self.posicao[1] + 192), (self.posicao[0]-posx + 78, self.posicao[1] + 192))
        button_ok = pygame.draw.polygon(SCREEN, (0, 0, 0, 0), list_point)
        SCREEN.blit(self.imagem_selecao, (self.posicao[0]-posx-25, self.posicao[1] + 100))

        fonte = pygame.font.Font("comic.ttf", config_caixa.data['caixa_tempo'][self.lingua]['tamanho'])
        texto = fonte.render(config_caixa.data['caixa_tempo'][self.lingua]['texto'], True, (0, 0, 0))
        SCREEN.blit(texto, (self.posicao[0]-posx +50 - texto.get_width()/2, self.posicao[1]))

        TELA = SCREEN.copy()

        texto = fonte.render(self.escreve[1:], True, (255, 255, 255))
        SCREEN.blit(texto, (self.posicao[0]-posx + 20, self.posicao[1] + 110))
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
                    SCREEN.blit(texto, (self.posicao[0]-posx + 20, self.posicao[1] + 110))
                    pygame.display.update((self.posicao[0]-posx, self.posicao[1] + 110, 100, 40))

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_ok.collidepoint(pygame.mouse.get_pos()):
                        self.tempo = float(self.escreve)
                        if self.tempo != 0.0:
                            print "OIUUUGGGG"
                            self.selecao_visivel = False
                            condicao = True

    def gera_texto(self):
        self.prog_text = ""
        self.prog_text += ("00-")
        self.prog_text += str(self.tempo)
        

    def recria(self,pos,tempo):
        self.escreve = tempo
        self.posicao = pos
        self.escreve = '0'+str(tempo)

    def gera_programa(self):
        self.prog_arduino = chr(0)
        time = int(self.tempo*10)
        print time
        while time > 250:
            self.prog_arduino += chr(250)
            time -= 250
            print time
            self.prog_arduino += chr(0)
        self.prog_arduino += chr(time)