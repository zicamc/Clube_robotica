# -*- coding: utf-8 -*-
import pygame
import pygame.font
from caixa import caixa
from configuracoes import config_caixa
from configuracoes import config_selecao

pygame.font.init()
#===============================================================================
#                   CAIXA TOQUE
#===============================================================================
class caixa_toque(caixa):
    def __init__(self):
        caixa.__init__(self)
        self.imagem = pygame.image.load("Imagens/Toque.gif").convert()
        self.imagem_selecao = pygame.image.load("Imagens/Caixa_toque.gif").convert()

        numero = int(config_selecao.data['caixa_toque']['numero'])
        for i in range(numero):
            fonte = pygame.font.Font("comic.ttf", config_selecao.data['caixa_toque'][self.lingua][i]['tamanho'])
            texto = fonte.render(config_selecao.data['caixa_toque'][self.lingua][i]['texto'], True, (0, 0, 0))
            pos = eval(config_selecao.data['caixa_toque'][self.lingua][i]['pos'])
            self.imagem_selecao.blit(texto,pos)


        self.opcoes = [True, False]
        self.sensores = [False, False]
        """ """

    def show(self, SCREEN, posx):
        if (self.posicao[0]-posx < 620 and self.posicao[0]-posx > -160):
            self.rect = SCREEN.blit(self.imagem, (self.posicao[0]-posx, self.posicao[1]))

            for i in range(len(self.opcoes)):
                if self.opcoes[i] == True:
                    break

            fonte = pygame.font.Font("comic.ttf", config_caixa.data['caixa_toque'][self.lingua]['opcoes'][i]['tamanho'])
            texto = fonte.render(config_caixa.data['caixa_toque'][self.lingua]['opcoes'][i]['texto'], True, (0, 0, 0))
            SCREEN.blit(texto, (self.posicao[0]-posx + 50 - texto.get_width()/2, self.posicao[1]))
            
            pos_y = self.posicao[1] + texto.get_height() - 5

            i = self.sensores[0] + self.sensores[1]*2
            numero = int(config_caixa.data['caixa_toque'][self.lingua]['selecao'][i]['numero'])

            for a in range(numero):
                fonte = pygame.font.Font("comic.ttf", config_caixa.data['caixa_toque'][self.lingua]['selecao'][i][a]['tamanho'])
                texto = fonte.render(config_caixa.data['caixa_toque'][self.lingua]['selecao'][i][a]['texto'], True, (0, 0, 0))
                SCREEN.blit(texto, (self.posicao[0]-posx + 50 - texto.get_width()/2 , pos_y)) 
                pos_y = pos_y + texto.get_height() - 5

            pygame.draw.line(SCREEN, (0, 0, 0, 0),
                             (self.posicao[0]-posx + 100, self.posicao[1] + 50),
                             (self.posicao[0]-posx + 125, self.posicao[1] + 50), 15)

            pygame.draw.polygon(SCREEN, (0, 0, 0, 0),
                                ((self.posicao[0]-posx + 125, self.posicao[1] + 25), (self.posicao[0]-posx + 125, self.posicao[1] + 75),
                                (self.posicao[0]-posx + 150, self.posicao[1] + 50)))
        else:
            self.rect = 0

    def events(self, SCREEN, posx):
        """ """
        SCREEN.blit(self.imagem, (self.posicao[0]-posx, self.posicao[1]))
        #Para não ficar trocando toda hora que clica em qualquer lugar e não colidir com os objetos apropriados
        colidiu = False

        # Será pelo menos esses, não sendo necessária a implementação de outros botões
        opcao1 = (self.posicao[0]-posx-16, self.posicao[1] + 132, 23, 19)
        opcao2 = (self.posicao[0]-posx-16, self.posicao[1] + 156, 23, 19)
        # Está sendo criada assim para facilicitação do inicio desta parte do
        # projeto, no futuro haverá outra interface que afetará esses botoes
        escolha1 = (self.posicao[0]-posx-16, self.posicao[1] + 201, 23, 19)
        escolha2 = (self.posicao[0]-posx-16, self.posicao[1] + 225, 23, 19)
        #Botao Ok
        points_ok = (self.posicao[0]-posx+21, self.posicao[1] + 248, 53, 28)

        botoes_opcoes = (pygame.draw.rect(SCREEN, (0, 0, 0, 0), opcao1),
                         pygame.draw.rect(SCREEN, (0, 0, 0, 0), opcao2))

        botoes_toque = (pygame.draw.rect(SCREEN, (0, 0, 0, 0), escolha1),
                        pygame.draw.rect(SCREEN, (0, 0, 0, 0), escolha2))

        botao_ok = pygame.draw.rect(SCREEN, (0, 0, 0, 0), points_ok)

        SCREEN.blit(self.imagem_selecao, (self.posicao[0]-posx-25, self.posicao[1] + 100))
        TELA = SCREEN.copy()
        self.botoes(SCREEN,posx,(opcao1[2],opcao1[3]))
        pygame.display.update((0, 0, 620, 600))

        condicao = False
        while condicao == False:
            self.treat_events()
            self.CLOCK.tick(15)
            for event in pygame.event.get(pygame.MOUSEBUTTONDOWN):
                if event.type == pygame.MOUSEBUTTONDOWN:

                    #OBS: como no máximo 3 coisas o motor poderá fazer e no minimo 2 opções, neste caso faremos sobre 2 opções
                    #OBS2: Melhorar essa forma, tá muito chinela, pensar em uma forma melhor
                    if botoes_opcoes[0].collidepoint(event.pos):
                        self.opcoes[0] = not(self.opcoes[0])
                        colidiu = True

                    elif botoes_opcoes[1].collidepoint(event.pos):
                        self.opcoes[1] = not(self.opcoes[1])
                        colidiu = True

                    elif botoes_toque[0].collidepoint(event.pos):
                        self.sensores[0] = not(self.sensores[0])
                        colidiu = True

                    elif botoes_toque[1].collidepoint(event.pos):
                        self.sensores[1] = not(self.sensores[1])
                        colidiu = True

                    elif botao_ok.collidepoint(event.pos):
                        # Testar se pelo menos uma selecao foi feita no sentido e nos motores, senão, trancar
                        teste_opcoes = self.opcoes[0] + self.opcoes[1]
                        teste_atuadores = self.sensores[0] + self.sensores[1]
                        if teste_opcoes == 1 and teste_atuadores > 0:
                            self.selecao_visivel = False
                            condicao = True
                        else:
                            print "Não entrei, pq uma das condições não foi satifeita"

                if colidiu == True:
                    colidiu = False
                    # Dá os blit das bolinhas de seleção, legal não!
                    # PS: Fiz do jeito feio de se fazer, cheio de if/else
                    SCREEN.blit(TELA, (0, 0))
                    self.botoes(SCREEN,posx,(opcao1[2],opcao1[3]))
                    pygame.display.update((self.posicao[0]-posx-16, self.posicao[1] + 128, 20, 200))
        """ """

    def botoes(self,SCREEN,posx, valor):
        if self.opcoes[0] == True:
            pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-16 + valor[0] / 2, self.posicao[1] + 133 + valor[1] / 2), 5)
        if self.opcoes[1] == True:
            pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-16 + valor[0] / 2, self.posicao[1] + 157 + valor[1] / 2), 5)
        if self.sensores[0] == True:
            pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-16 + valor[0] / 2, self.posicao[1] + 201 + valor[1] / 2), 5)
        if self.sensores[1] == True:
            pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-16 + valor[0] / 2, self.posicao[1] + 225 + valor[1] / 2), 5)

    def gera_texto(self):
        if self.opcoes[0] == True:
            self.prog_text = "05-"
        else:
            self.prog_text = "06-"

        self.prog_text += str(int(self.sensores[0]))
        self.prog_text += str(int(self.sensores[1]))

    def recria(self,pos,ID,prog):

        self.posicao = pos

        if ID == '05':
            self.opcoes[0] = True
            self.opcoes[1] = False
        else:
            self.opcoes[0] = False
            self.opcoes[1] = True

        self.sensores[0] = bool(int(prog[0]))
        self.sensores[1] = bool(int(prog[1]))

    def gera_programa(self):

        if self.opcoes[0]:
            self.prog_arduino = chr(5)
        else:
            self.prog_arduino = chr(6)

        self.prog_arduino = chr(self.opcoes[0]+self.opcoes[1]*2)