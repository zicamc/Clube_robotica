# -*- coding: utf-8 -*-

import sys

import pygame
import pygame.font

pygame.font.init()
CLOCK = pygame.time.Clock()
fonte = pygame.font.Font("comic.ttf", 25)

class caixa():
    def __init__(self):
        pass
    def troca_posicao(self, posicao):
        pass
    def troca_posicaox(self, posicao):
        pass
    def show(self, SCREEN, posx):
        pass
    def colide(self, pos):
        pass

    
    def events(self, SCREEN, posx):
        pass
    def retorna_pos(self):
        pass
class caixa_inicio(caixa):
    def __init__(self):
        """

        """
        self.posicao = (20, 150)
        self.imagem = pygame.image.load("Imagens/Inicio.gif").convert()
        self.posx = 0
        self.progama = -1
        """

        """

    def troca_posicaox(self, posicao):
        """
        
        """
        self.posx = posicao
        """
        
        """

    def show(self, SCREEN, posx):
        """

        """
        if (self.posicao[0]-posx < 620 or self.posicao[0]-posx > 0):
            SCREEN.blit(self.imagem, (self.posicao[0]-posx, self.posicao[1]))
            pygame.draw.line(SCREEN, (0, 0, 0, 0),
                             (self.posicao[0]-posx + 50, self.posicao[1] + 50),
                             (self.posicao[0]-posx + 75, self.posicao[1] + 50), 15)
            pygame.draw.polygon(SCREEN, (0, 0, 0, 0),
                                ((self.posicao[0]-posx + 75, self.posicao[1] + 25), (self.posicao[0]-posx + 75, self.posicao[1] + 75),
                                (self.posicao[0]-posx + 100, self.posicao[1] + 50)))
            pygame.display.update((self.posicao[0]-posx, self.posicao[1], 90-posx, 100))
        """

        """
    def colide(self, pos):
        """

        """
        return 0

class caixa_tempo(caixa):
    def __init__(self):
        """

        """
        self.imagem = pygame.image.load("Imagens/delay.gif").convert()
        self.rect = 0
        self.posicao = (0, 0)

        self.imagem_selecao = pygame.image.load("Imagens/Caixa_tempo.gif").convert()
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

            texto = font.render(self.escreve[1:], True, (0, 0, 0))

            SCREEN.blit(texto, (self.posicao[0]-posx + 20, self.posicao[1] + 50))

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

        TELA = SCREEN.copy()

        texto = fonte.render(self.escreve[1:], True, (255, 255, 255))
        SCREEN.blit(texto, (self.posicao[0]-posx + 20, self.posicao[1] + 110))
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
                    SCREEN.blit(texto, (self.posicao[0]-posx + 20, self.posicao[1] + 110))
                    pygame.display.update((self.posicao[0]-posx, self.posicao[1] + 110, 100, 40))

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

class caixa_motor(caixa):
    def __init__(self):
        """ """
        self.imagem = pygame.image.load("Imagens/Motor.gif").convert()
        self.rect = 0
        self.posicao = (0, 0)

        self.imagem_selecao = pygame.image.load("Imagens/Caixa_motor.gif").convert()
        self.opcoes = [True, False]
        self.atuadores = [False, False]
        """ """

    def troca_posicao(self, posicao):
        """ """
        self.posicao = posicao
        """ """

    def show(self, SCREEN, posx):
        """ """
        if (self.posicao[0]-posx < 620 and self.posicao[0]-posx > -160):
            font = pygame.font.Font("comic.ttf", 25)
            self.rect = SCREEN.blit(self.imagem, (self.posicao[0]-posx, self.posicao[1]))

            if self.opcoes[0] == True:
                texto = font.render("Frente", True, (0, 0, 0))
                SCREEN.blit(texto, (self.posicao[0]-posx + 10, self.posicao[1] + 25))
            else:
                texto = font.render("Parar", True, (0, 0, 0))
                SCREEN.blit(texto, (self.posicao[0]-posx + 15, self.posicao[1] + 25))
            
            font = pygame.font.Font("comic.ttf", 20)

            if self.atuadores[0] == True and self.atuadores[1] == False:
                texto = font.render("Dir", True, (0, 0, 0))
                SCREEN.blit(texto, (self.posicao[0]-posx + 33, self.posicao[1] + 60))

            elif self.atuadores[0] == True and self.atuadores[1] == True:
                texto = font.render("Dir & Esq", True, (0, 0, 0))
                SCREEN.blit(texto, (self.posicao[0]-posx + 4, self.posicao[1] + 60))

            elif self.atuadores[1] == True and self.atuadores[0] == False:
                texto = font.render("Esq", True, (0, 0, 0))
                SCREEN.blit(texto, (self.posicao[0]-posx + 33, self.posicao[1] + 60))

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
        SCREEN.blit(self.imagem, (self.posicao[0]-posx, self.posicao[1]))
        #Para não ficar trocando toda hora que clica em qualquer lugar e não colidir com os objetos apropriados
        colidiu = False

        # Será pelo menos esses, não sendo necessária a implementação de outros botões
        opcao1 = (self.posicao[0]-posx-16, self.posicao[1] + 128, 23, 19)
        opcao2 = (self.posicao[0]-posx-16, self.posicao[1] + 152, 23, 19)
        # Está sendo criada assim para facilicitação do inicio desta parte do
        # projeto, no futuro haverá outra interface que afetará esses botoes
        escolha1 = (self.posicao[0]-posx-16, self.posicao[1] + 222, 23, 19)
        escolha2 = (self.posicao[0]-posx-16, self.posicao[1] + 246, 23, 19)
        #Botao Ok
        points_ok = (self.posicao[0]-posx-4, self.posicao[1] + 269, 53, 28)

        botoes_opcoes = (pygame.draw.rect(SCREEN, (0, 0, 0, 0), opcao1),
                         pygame.draw.rect(SCREEN, (0, 0, 0, 0), opcao2))

        botoes_atuadores = (pygame.draw.rect(SCREEN, (0, 0, 0, 0), escolha1),
                            pygame.draw.rect(SCREEN, (0, 0, 0, 0), escolha2))

        botao_ok = pygame.draw.rect(SCREEN, (0, 0, 0, 0), points_ok)

        SCREEN.blit(self.imagem_selecao, (self.posicao[0]-posx-25, self.posicao[1] + 100))
        TELA = SCREEN.copy()
        #Draw do primeiro botão selecionador
        if self.opcoes[0] == True:
            pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-16 + opcao1[2] / 2, self.posicao[1] + 128 + opcao1[3] / 2), 5)
        if self.opcoes[1] == True:
            pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-16 + opcao2[2] / 2, self.posicao[1] + 152 + opcao2[3] / 2), 5)

        if self.atuadores[0] == True:
            pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-16 + escolha1[2] / 2, self.posicao[1] + 222 + escolha1[3] / 2), 5)
        if self.atuadores[1] == True:
            pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-16 + escolha2[2] / 2, self.posicao[1] + 246 + escolha2[3] / 2), 5)
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

                    elif botoes_atuadores[0].collidepoint(event.pos):
                        self.atuadores[0] = not(self.atuadores[0])
                        colidiu = True

                    elif botoes_atuadores[1].collidepoint(event.pos):
                        self.atuadores[1] = not(self.atuadores[1])
                        colidiu = True

                    elif botao_ok.collidepoint(event.pos):
                        # Testar se pelo menos uma selecao foi feita no sentido e nos motores, senão, trancar
                        teste_opcoes = self.opcoes[0] + self.opcoes[1]
                        teste_atuadores = self.atuadores[0] + self.atuadores[1]
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
                        pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-16 + opcao1[2] / 2, self.posicao[1] + 128 + opcao1[3] / 2), 5)
                    if self.opcoes[1] == True:
                        pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-16 + opcao2[2] / 2, self.posicao[1] + 152 + opcao2[3] / 2), 5)

                    if self.atuadores[0] == True:
                        pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-16 + escolha1[2] / 2, self.posicao[1] + 222 + escolha1[3] / 2), 5)
                    if self.atuadores[1] == True:
                        pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-16 + escolha2[2] / 2, self.posicao[1] + 246 + escolha2[3] / 2), 5)
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

class caixa_led(caixa):
    def __init__(self):
        self.imagem = pygame.image.load("Imagens/LED.gif").convert()
        self.rect = 0
        self.posicao = (0, 0)

        self.imagem_selecao = pygame.image.load("Imagens/Caixa_led.gif").convert()
        self.opcoes = [True, False]
        self.leds = [False, False, False]
        """ """

    def troca_posicao(self, posicao):
        """ """
        self.posicao = posicao
        """ """

    def show(self, SCREEN, posx):
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