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
#                   CAIXA TOQUE
#===============================================================================
class caixa_toque(caixa):
    def __init__(self):
        self.imagem = pygame.image.load("Imagens/Toque.gif").convert()
        self.rect = 0
        self.posicao = (0, 0)
        self.lingua = all_config.data['lingua']

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

    def troca_posicao(self, posicao):
        """ """
        self.posicao = posicao
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
        #Draw do primeiro botão selecionador
        if self.opcoes[0] == True:
            pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-16 + opcao1[2] / 2, self.posicao[1] + 133 + opcao1[3] / 2), 5)
        if self.opcoes[1] == True:
            pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-16 + opcao2[2] / 2, self.posicao[1] + 157 + opcao2[3] / 2), 5)

        if self.sensores[0] == True:
            pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-16 + escolha1[2] / 2, self.posicao[1] + 201 + escolha1[3] / 2), 5)
        if self.sensores[1] == True:
            pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-16 + escolha2[2] / 2, self.posicao[1] + 225 + escolha2[3] / 2), 5)
        pygame.display.update((0, 0, 620, 600))

        condicao = False
        while condicao == False:
            treat_events()
            CLOCK.tick(15)
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
                    if self.opcoes[0] == True:
                        pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-16 + opcao1[2] / 2, self.posicao[1] + 133 + opcao1[3] / 2), 5)
                    if self.opcoes[1] == True:
                        pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-16 + opcao2[2] / 2, self.posicao[1] + 157 + opcao2[3] / 2), 5)

                    if self.sensores[0] == True:
                        pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-16 + escolha1[2] / 2, self.posicao[1] + 201 + escolha1[3] / 2), 5)
                    if self.sensores[1] == True:
                        pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-16 + escolha2[2] / 2, self.posicao[1] + 225 + escolha2[3] / 2), 5)
                    pygame.display.update((self.posicao[0]-posx-16, self.posicao[1] + 128, 20, 200))

        """ """


    def colide(self, pos):
        """ """
        try:
            return self.rect.collidepoint(pos)
        except:
            return 0
        """ """

    def retorna_pos(self):
        """ """
        return self.posicao
        """ """

def treat_events():
    """
    Função que verifica se algo aconteceu para que o programa se feche. Aqui por preguica, nao tava afim de faze um import!
    """
    # Criar uma thread para isso
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                                           sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:     sys.exit()

    """ """
