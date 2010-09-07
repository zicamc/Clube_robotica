# -*- coding: utf-8 -*-
import pygame
import pygame.font
from caixa import caixa
from configuracoes import config_caixa
from configuracoes import config_selecao
pygame.font.init()
fonte = pygame.font.Font("comic.ttf", 25)
#===============================================================================
#                   CAIXA TEMPERATURA
#===============================================================================
class caixa_temperatura(caixa):
    """

    """
    def __init__(self):
        caixa.__init__(self)
        self.imagem = pygame.image.load("Imagens/temperatura.gif").convert()

        self.imagem_selecao = pygame.image.load("Imagens/caixa_temp.gif").convert()

        numero = int(config_selecao.data['caixa_temperatura']['numero'])
        for i in range(numero):
            fonte = pygame.font.Font("comic.ttf", config_selecao.data['caixa_temperatura'][self.lingua][i]['tamanho'])
            texto = fonte.render(config_selecao.data['caixa_temperatura'][self.lingua][i]['texto'], True, (0, 0, 0))
            pos = eval(config_selecao.data['caixa_temperatura'][self.lingua][i]['pos'])
            self.imagem_selecao.blit(texto,pos)

        self.opcoes = [True, False]

        self.tempo = 0.0
        self.escreve = "0"
        """ """

    def show(self, SCREEN, posx):
        if (self.posicao[0]-posx < 620 and self.posicao[0]-posx > -160):
            self.rect = SCREEN.blit(self.imagem, (self.posicao[0]-posx, self.posicao[1]))
            fonte = pygame.font.Font("comic.ttf", 20)
            #Aqui vão os textos

            for i in range(len(self.opcoes)):
                if self.opcoes[i] == True:
                    break

            numero = int(config_caixa.data['caixa_luz'][self.lingua][i]['numero'])

            pos_y = 2

            for a in range(numero):
                fonte = pygame.font.Font("comic.ttf", config_caixa.data['caixa_temperatura'][self.lingua][i][a]['tamanho'])
                texto = fonte.render(config_caixa.data['caixa_temperatura'][self.lingua][i][a]['texto'], True, (0, 0, 0))
                SCREEN.blit(texto, (self.posicao[0]-posx + 50 - texto.get_width()/2 , self.posicao[1] + pos_y))
                pos_y = pos_y + texto.get_height() - 4

            #Texto do tempo centralizado
            fonte = pygame.font.Font("comic.ttf", 25)
            texto = fonte.render(self.escreve[1:]+"s", True, (0, 0, 0))
            tam_text = texto.get_width()/2
            SCREEN.blit(texto, (self.posicao[0]-posx+50-tam_text , self.posicao[1] + pos_y + 10 ))

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

        #Botao Ok
        points_ok = (self.posicao[0]-posx+21, self.posicao[1] + 248, 53, 28)

        botoes_opcoes = (pygame.draw.rect(SCREEN, (0, 0, 0, 0), opcao1),
                         pygame.draw.rect(SCREEN, (0, 0, 0, 0), opcao2))


        botao_ok = pygame.draw.rect(SCREEN, (0, 0, 0, 0), points_ok)

        SCREEN.blit(self.imagem_selecao, (self.posicao[0]-posx-25, self.posicao[1] + 100))

        TELA = SCREEN.copy()
        if self.opcoes[0] == True:
            pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-14 + opcao1[2] / 2, self.posicao[1] + 130 + opcao1[3] / 2), 5)
        if self.opcoes[1] == True:
            pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-14 + opcao2[2] / 2, self.posicao[1] + 154 + opcao2[3] / 2), 5)
        texto = fonte.render(self.escreve[1:], True, (255, 255, 255))
        SCREEN.blit(texto, (self.posicao[0]-posx + 20, self.posicao[1] + 210))
        pygame.display.update((0, 0, 620, 600))

        condicao = False
        while condicao == False:
            self.treat_events()
            self.CLOCK.tick(15)
            for event in pygame.event.get((pygame.MOUSEBUTTONDOWN,pygame.KEYDOWN)):
                if event.type == pygame.KEYDOWN:
                    colidiu = True
                    key = event.key
                    self.teclado_numerico(key)

                elif event.type == pygame.MOUSEBUTTONDOWN:

                    if botoes_opcoes[0].collidepoint(event.pos):
                        colidiu = True
                        self.opcoes[0] = not(self.opcoes[0])
                    elif botoes_opcoes[1].collidepoint(event.pos):
                        colidiu = True
                        self.opcoes[1] = not(self.opcoes[1])


                    if botao_ok.collidepoint(event.pos):
                        # Testar se pelo menos uma selecao foi feita no sentido e nos motores, senão, trancar
                        teste_opcoes = self.opcoes[0] + self.opcoes[1]
                        try:
                            self.tempo = float(self.escreve)
                        except:
                            self.tempo = 0
                        if teste_opcoes == 1 and self.tempo > 0:
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
                    pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-14 + opcao1[2] / 2, self.posicao[1] + 130 + opcao1[3] / 2), 5)
                if self.opcoes[1] == True:
                    pygame.draw.circle(SCREEN, (0, 0, 0, 0), (self.posicao[0]-posx-14 + opcao2[2] / 2, self.posicao[1] + 154 + opcao2[3] / 2), 5)

                texto = fonte.render(self.escreve[1:], True, (255, 255, 255))
                SCREEN.blit(texto, (self.posicao[0]-posx + 20, self.posicao[1] + 210))
                pygame.display.update((self.posicao[0]-posx-25, self.posicao[1] + 100, 100, 200))

    def gera_texto(self):
        if self.opcoes[0] == True:
            self.prog_text = "07-"
        else:
            self.prog_text = "08-"

        self.prog_text += str(self.tempo)

    def recria(self,pos,ID,tempo):

        self.posicao = pos

        if ID == '07':
            self.opcoes[0] = True
            self.opcoes[1] = False
        else:
            self.opcoes[0] = False
            self.opcoes[1] = True

        self.tempo = tempo
        self.escreve = '0'+str(tempo)

    def gera_programa(self):

        if self.opcoes[0]:
            temp = 7
        else:
            temp = 8

        self.prog_arduino = chr(temp)
        time = int(self.tempo*10)
        print time
        while time > 250:
            self.prog_arduino += chr(250)
            time -= 250
            print time
            self.prog_arduino += chr(temp)
        self.prog_arduino += chr(time)