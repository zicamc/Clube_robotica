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
#                   CAIXA MOTOR
#===============================================================================

class caixa_motor(caixa):
    def __init__(self):
        """ """
        self.imagem = pygame.image.load("Imagens/Motor.gif").convert()
        self.rect = 0
        self.posicao = (0, 0)
        self.lingua = all_config.data['lingua']

        #Cria imagem motor conforme selecao
        self.imagem_selecao = pygame.image.load("Imagens/Caixa_motor.gif").convert()
        numero = int(config_selecao.data['caixa_motor']['numero'])
        for i in range(numero):
            fonte = pygame.font.Font("comic.ttf", config_selecao.data['caixa_motor'][self.lingua][i]['tamanho'])
            texto = fonte.render(config_selecao.data['caixa_motor'][self.lingua][i]['texto'], True, (0, 0, 0))
            pos = eval(config_selecao.data['caixa_motor'][self.lingua][i]['pos'])
            self.imagem_selecao.blit(texto,pos)

        self.opcoes = [False, False, False, False]
        """ """

    def troca_posicao(self, posicao):
        """ """
        self.posicao = posicao
        """ """

    def show(self, SCREEN, posx):
        """ """
        if (self.posicao[0]-posx < 620 and self.posicao[0]-posx > -160):
            self.rect = SCREEN.blit(self.imagem, (self.posicao[0]-posx, self.posicao[1]))
            
            for i in range(len(self.opcoes)):
                if self.opcoes[i] == True:
                    break

            numero = config_caixa.data['caixa_motor'][self.lingua][i]['numero']

            for a in range(numero):
                fonte = pygame.font.Font("comic.ttf", config_caixa.data['caixa_motor'][self.lingua][i][a]['tamanho'])
                texto = fonte.render(config_caixa.data['caixa_motor'][self.lingua][i][a]['texto'], True, (0, 0, 0))
                pos = eval(config_caixa.data['caixa_motor'][self.lingua][i][a]['pos'])
                SCREEN.blit(texto, (self.posicao[0]-posx + pos[0], self.posicao[1] + pos[1]))
                
            pygame.draw.line(SCREEN, (0, 0, 0, 0),
                             (self.posicao[0]-posx + 100, self.posicao[1] + 50),
                             (self.posicao[0]-posx + 125, self.posicao[1] + 50), 15)

            pygame.draw.polygon(SCREEN, (0, 0, 0, 0),
                                ((self.posicao[0]-posx + 125, self.posicao[1] + 25), (self.posicao[0]-posx + 125, self.posicao[1] + 75),
                                (self.posicao[0]-posx + 150, self.posicao[1] + 50)))
        else:
            self.rect = 0
        """ """


    def events(self, SCREEN, posx):
        """ """

        #ANDA PARA FRENTE, ANDRA PARA ESQUERDA, ANDA PARA DIREITA

        SCREEN.blit(self.imagem, (self.posicao[0]-posx, self.posicao[1]))
        #Para não ficar trocando toda hora que clica em qualquer lugar e não colidir com os objetos apropriados
        colidiu = False

        # Será pelo menos esses, não sendo necessária a implementação de outros botões
        opcao1 = (self.posicao[0]-posx-21, self.posicao[1] + 129, 23, 19)
        opcao2 = (self.posicao[0]-posx-21, self.posicao[1] + 151, 23, 19)
        opcao3 = (self.posicao[0]-posx-21, self.posicao[1] + 175, 23, 19)
        opcao4 = (self.posicao[0]-posx-21, self.posicao[1] + 200, 23, 19)
        #Botao Ok
        points_ok = (self.posicao[0]-posx-4, self.posicao[1] + 228, 53, 28)

        botoes_opcoes = (pygame.draw.rect(SCREEN, (0, 0, 0, 0), opcao1),
                         pygame.draw.rect(SCREEN, (0, 0, 0, 0), opcao2),
                         pygame.draw.rect(SCREEN, (0, 0, 0, 0), opcao3),
                         pygame.draw.rect(SCREEN, (0, 0, 0, 0), opcao4))

        botao_ok = pygame.draw.rect(SCREEN, (0, 0, 0, 0), points_ok)

        SCREEN.blit(self.imagem_selecao, (self.posicao[0]-posx-25, self.posicao[1] + 100))
        TELA = SCREEN.copy()
        #Draw do primeiro botão selecionador
        if self.opcoes[0] == True:
            pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-21 + opcao1[2] / 2, self.posicao[1] + 128 + opcao1[3] / 2), 5)
        if self.opcoes[1] == True:
            pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-21 + opcao2[2] / 2, self.posicao[1] + 152 + opcao2[3] / 2), 5)
        if self.opcoes[2] == True:
            pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-21 + opcao3[2] / 2, self.posicao[1] + 176 + opcao3[3] / 2), 5)
        if self.opcoes[3] == True:
            pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-21 + opcao4[2] / 2, self.posicao[1] + 200 + opcao4[3] / 2), 5)

        pygame.display.update((0, 0, 620, 600))

        condicao = False
        while condicao == False:
            treat_events()
            CLOCK.tick(15)
            for event in pygame.event.get(pygame.MOUSEBUTTONDOWN):
                if botoes_opcoes[0].collidepoint(event.pos):
                    self.opcoes[0] = not(self.opcoes[0])
                    colidiu = True
                    continue

                if botoes_opcoes[1].collidepoint(event.pos):
                    print "Colidi"
                    self.opcoes[1] = not(self.opcoes[1])
                    colidiu = True
                    continue

                if botoes_opcoes[2].collidepoint(event.pos):
                    self.opcoes[2] = not(self.opcoes[2])
                    colidiu = True
                    continue

                if botoes_opcoes[3].collidepoint(event.pos):
                    self.opcoes[3] = not(self.opcoes[3])
                    colidiu = True
                    continue

                if botao_ok.collidepoint(event.pos):
                    # Testar se pelo menos uma selecao foi feita no sentido e nos motores, senão, trancar
                    teste_opcoes = self.opcoes[0] + self.opcoes[1] + self.opcoes[2] + self.opcoes[3]
                    if teste_opcoes == 1:
                        self.selecao_visivel = False
                        condicao = True
                    else:
                        print "Não entrei, pq uma das condições não foi satifeita"
                    continue

            if colidiu == True:
                colidiu = False
                # PS: Fiz do jeito feio de se fazer, cheio de if/else
                SCREEN.blit(TELA, (0, 0))
                if self.opcoes[0] == True:
                    pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-21 + opcao1[2] / 2, self.posicao[1] + 128 + opcao1[3] / 2), 5)
                if self.opcoes[1] == True:
                    pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-21 + opcao2[2] / 2, self.posicao[1] + 152 + opcao2[3] / 2), 5)
                if self.opcoes[2] == True:
                    pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-21 + opcao3[2] / 2, self.posicao[1] + 176 + opcao3[3] / 2), 5)
                if self.opcoes[3] == True:
                    pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-21 + opcao4[2] / 2, self.posicao[1] + 200 + opcao4[3] / 2), 5)
                pygame.display.update((self.posicao[0]-posx-21, self.posicao[1] + 128, 20, 200))
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
