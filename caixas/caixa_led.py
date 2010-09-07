# -*- coding: utf-8 -*-
import pygame
import pygame.font
from caixa import caixa
from configuracoes import config_caixa
from configuracoes import config_selecao

pygame.font.init()

#===============================================================================
#                   CAIXA LED
#===============================================================================
class caixa_led(caixa):
    def __init__(self):
        caixa.__init__(self)

        self.imagem = pygame.image.load("Imagens/LED.gif").convert()
        self.imagem_selecao = pygame.image.load("Imagens/Caixa_led.gif").convert()
        numero = int(config_selecao.data['caixa_led']['numero'])
        for i in range(numero):
            fonte = pygame.font.Font("comic.ttf", config_selecao.data['caixa_led'][self.lingua][i]['tamanho'])
            texto = fonte.render(config_selecao.data['caixa_led'][self.lingua][i]['texto'], True, (0, 0, 0))
            pos = eval(config_selecao.data['caixa_led'][self.lingua][i]['pos'])
            self.imagem_selecao.blit(texto,pos)

        self.opcoes = [True, False]
        self.leds = [False, False, False]
        """ """

    def show(self, SCREEN, posx):
        
        if (self.posicao[0]-posx < 620 and self.posicao[0]-posx > -160):
            self.rect = SCREEN.blit(self.imagem, (self.posicao[0]-posx, self.posicao[1]))

            for i in range(len(self.opcoes)):
                if self.opcoes[i] == True:
                    break

            fonte = pygame.font.Font("comic.ttf", config_caixa.data['caixa_led'][self.lingua][i]['tamanho'])
            texto = fonte.render(config_caixa.data['caixa_led'][self.lingua][i]['texto'], True, (0, 0, 0))
            SCREEN.blit(texto, (self.posicao[0] -posx + 50 - texto.get_width()/2 , self.posicao[1]))
            pos_y = self.posicao[1] + texto.get_height() - 5
            
            i = self.leds[0] + self.leds[1]*2 + self.leds[2]*4
            numero = int(config_caixa.data['caixa_led']['selecao'][i]['numero'])

            for a in range(numero):
                fonte = pygame.font.Font("comic.ttf", config_caixa.data['caixa_led']['selecao'][i][a]['tamanho'])
                texto = fonte.render(config_caixa.data['caixa_led']['selecao'][i][a]['texto'], True, (0, 0, 0))
                SCREEN.blit(texto, (self.posicao[0]-posx + 50 - texto.get_width()/2, pos_y))
                pos_y = pos_y + texto.get_height() - 5
                
            pygame.draw.line(SCREEN, (0, 0, 0, 0),
                             (self.posicao[0]-posx + 100, self.posicao[1] + 50),
                             (self.posicao[0]-posx + 125, self.posicao[1] + 50), 15)

            pygame.draw.polygon(SCREEN, (0, 0, 0, 0),
                                ((self.posicao[0]-posx + 125, self.posicao[1] + 25), (self.posicao[0]-posx + 125, self.posicao[1] + 75),
                                (self.posicao[0]-posx + 150, self.posicao[1] + 50)))
        else:
            self.rect = 0
        pass

    def events(self, SCREEN, posx):
        """ """
        SCREEN.blit(self.imagem, (self.posicao[0]-posx, self.posicao[1]))
        #Para não ficar trocando toda hora que clica em qualquer lugar e não colidir com os objetos apropriados
        colidiu = False

        # Será pelo menos esses, não sendo necessária a implementação de outros botões
        opcao1 = (self.posicao[0]-posx-15, self.posicao[1] + 132, 23, 19)
        opcao2 = (self.posicao[0]-posx-15, self.posicao[1] + 156, 23, 19)

        # Está sendo criada assim para facilicitação do inicio desta parte do
        # projeto, no futuro haverá outra interface que afetará esses botoes
        escolha1 = (self.posicao[0]-posx-15, self.posicao[1] + 204, 23, 19)
        escolha2 = (self.posicao[0]-posx-15, self.posicao[1] + 223, 23, 19)
        escolha3 = (self.posicao[0]-posx-15, self.posicao[1] + 240, 23, 19)

        #Botao Ok
        points_ok = (self.posicao[0]-posx + 10, self.posicao[1] + 266, 53, 28)

        botoes_opcoes = (pygame.draw.rect(SCREEN, (0, 0, 0, 0), opcao1),
                         pygame.draw.rect(SCREEN, (0, 0, 0, 0), opcao2))


        botoes_leds = (pygame.draw.rect(SCREEN, (0, 0, 0, 0), escolha1),
                       pygame.draw.rect(SCREEN, (0, 0, 0, 0), escolha2),
                       pygame.draw.rect(SCREEN, (0, 0, 0, 0), escolha3))

        botao_ok = pygame.draw.rect(SCREEN, (0, 0, 0, 0), points_ok)

        SCREEN.blit(self.imagem_selecao, (self.posicao[0]-posx-25, self.posicao[1] + 100))
        TELA = SCREEN.copy()
        
        if self.opcoes[0] == True:
            pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-15 + opcao1[2] / 2, self.posicao[1] + 132 + opcao1[3] / 2), 5)
        if self.opcoes[1] == True:
            pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-15 + opcao2[2] / 2, self.posicao[1] + 156 + opcao2[3] / 2), 5)

        if self.leds[0] == True:
            pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-15 + escolha1[2] / 2, self.posicao[1] + 204 + escolha1[3] / 2), 5)
        if self.leds[1] == True:
            pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-15 + escolha2[2] / 2, self.posicao[1] + 223 + escolha2[3] / 2), 5)
        if self.leds[2] == True:
            pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-15 + escolha3[2] / 2, self.posicao[1] + 240 + escolha3[3] / 2), 5)

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

                    elif botoes_leds[0].collidepoint(event.pos):
                        self.leds[0] = not(self.leds[0])
                        colidiu = True

                    elif botoes_leds[1].collidepoint(event.pos):
                        self.leds[1] = not(self.leds[1])
                        colidiu = True
                    
                    elif botoes_leds[2].collidepoint(event.pos):
                        self.leds[2] = not(self.leds[2])
                        colidiu = True

                    elif botao_ok.collidepoint(event.pos):
                        # Testar se pelo menos uma selecao foi feita na ação do led e nos leds, senão, trancar
                        teste_opcoes = self.opcoes[0] + self.opcoes[1]
                        teste_atuadores = self.leds[0] + self.leds[1] + self.leds[2]
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
                        pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-15 + opcao1[2] / 2, self.posicao[1] + 132 + opcao1[3] / 2), 5)
                    if self.opcoes[1] == True:
                        pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-15 + opcao2[2] / 2, self.posicao[1] + 156 + opcao2[3] / 2), 5)

                    if self.leds[0] == True:
                        pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-15 + escolha1[2] / 2, self.posicao[1] + 204 + escolha1[3] / 2), 5)
                    if self.leds[1] == True:
                        pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-15 + escolha2[2] / 2, self.posicao[1] + 223 + escolha2[3] / 2), 5)
                    if self.leds[2] == True:
                        pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-15 + escolha3[2] / 2, self.posicao[1] + 240 + escolha3[3] / 2), 5)

                    pygame.display.update((self.posicao[0]-posx-16, self.posicao[1] + 128, 20, 200))

        """
        """
    def gera_texto(self):
        self.prog_text = ""
        self.prog_text += ("01-")
        self.prog_text += str(int(self.opcoes[0]))
        self.prog_text += str(int(self.opcoes[1]))
        self.prog_text += str(int(self.leds[0]))
        self.prog_text += str(int(self.leds[1]))
        self.prog_text += str(int(self.leds[2]))

    def recria(self,pos,prog):
        self.posicao = pos
        self.opcoes[0] = bool(int(prog[0]))
        self.opcoes[1] = bool(int(prog[1]))
        self.leds[0] = bool(int(prog[2]))
        self.leds[1] = bool(int(prog[3]))
        self.leds[2] = bool(int(prog[4]))

    def gera_programa(self):
        self.prog_arduino = ""

        if self.opcoes[0] == True:
            temp = 1
        else:
            temp = 2

        if self.leds[0] == True:
            self.prog_arduino += chr(temp)
            self.prog_arduino += chr(0)
        if self.leds[1] == True:
            self.prog_arduino += chr(temp)
            self.prog_arduino += chr(1)
        if self.leds[2] == True:
            self.prog_arduino += chr(temp)
            self.prog_arduino += chr(2)