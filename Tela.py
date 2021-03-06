# -*- coding: utf-8 -*-
# To change this template, choose Tools | Templates
# and open the template in the editor.

import pygame
from caixas.configuracoes import *
from palette import Palette
from work_area import Work_Area
from serial import Serial_Arduino
from arquivos import Arquivos

class tela(object):
    """
    Está é a classe que gerenciará a tela, tudo que estiver na tela, ou qualquer
    modificação será gerenciado por essa classe
    """

    def __init__(self):
        #Variáveis para criação da tela
        self.SIZE = eval( all_config.data["tamanho_tela"])
        self.SCREEN = pygame.display.set_mode(self.SIZE)
        self.objWorkArea = Work_Area()
        self.objPalette  = Palette()
        self.objSerial =  Serial_Arduino()
        self.CLOCK = pygame.time.Clock()
        self.file = Arquivos()

        #Cria os rects 
        print "Lista de rects criados para a palette:"
        
    def inicia_screen(self):
        """
        É um método que inicia a tela ou SCREEN
        """
        print "Iniciando show_screen"
        self.objWorkArea.mostra_workarea(self.SCREEN)
        self.objPalette.mostra_palette(self.SCREEN)
        pygame.display.update()
        print "\tFinalizando show_screen"


    def drag_and_drop(self, tuple_caixa):
        """
        Esta função é a que faz o drag and drop de toda a interface, ou seja, quando clicar em algo que possui uma caixa
        ela irá funcionar como um drag and drop.
        """
        caixa = tuple_caixa[0]
        # MELHORAR ESTE CÓDIGO, ESTÁ A CONSUMIR MUITO PROCESSAMENTO
        teste = 0
        pos_anterior = (0,0)
        TELA = self.SCREEN.copy()
        while teste == 0:
            self.CLOCK.tick(10)
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                self.SCREEN.blit(TELA,(0,0))
                caixa.show_em_nova_posicao( self.SCREEN,(pos[0]-50,pos[1]-50))
                if event.type == pygame.MOUSEBUTTONUP:
                    posv = self.objWorkArea.retorna_posv()
                    posx = self.objWorkArea.retorna_posx()
                    variacao = 0
                    if ( posv - posx > 520 or posv - posx < 0):
                        variacao = (posv - posx) - 310;
                        self.objWorkArea.modifica_posx(posx + variacao)
                    self.objWorkArea.mostra_workarea(self.SCREEN)
                    self.objPalette.mostra_palette(self.SCREEN)
                    pygame.display.update()
                    self.objWorkArea.nova_caixa(self.SCREEN, (pos[0]-variacao,pos[1]), tuple_caixa[1])
                    teste = 1
                pygame.display.update((pos_anterior[0]-50,pos_anterior[1]-50, 100, 100))
                pygame.display.update((pos[0]-50,pos[1]-50,100,100))
                pos_anterior = pos

        print "SAi do While"
        self.SCREEN.blit(TELA,(0,0))
        pygame.display.update()
    
    """"""

    def acoes(self):
        """
        Esta função é a que irá atualizar, adicionar/remover e verificar as modificações feitas pelo usuário.
        """
        for event in pygame.event.get(pygame.MOUSEBUTTONDOWN):
            posicao = event.pos
            if posicao[1] > 540:
                temp = self.objWorkArea.teste_botoes(posicao)
                if temp != -1:
                    self.botoes_Tela(temp)

            elif posicao[0] > 620:
                temp = self.objPalette.verifica_palette( posicao )
                if temp == 1:
                    print "Troca de palette"
                    self.objPalette.mostra_palette(self.SCREEN)
                elif temp == 0:
                    print "Não faz drag and drop"
                    pass
                else:
                    "Faz drag and drop"
                    print temp
                    self.drag_and_drop(temp)
                    self.objWorkArea.mostra_workarea(self.SCREEN)
                    self.objPalette.mostra_palette(self.SCREEN)
                    pygame.display.update()
            else:
                if event.button == 1: #TODO 1 significa que o botão clicado foi o da direita
                    if (self.objWorkArea.modifica_caixa(self.SCREEN,posicao) == 1):
                        self.objWorkArea.mostra_workarea(self.SCREEN)
                        self.objPalette.mostra_palette(self.SCREEN)
                        pygame.display.update()

                elif event.button == 3:
                    if (self.objWorkArea.retira_caixa(posicao) == 1):
                        self.objWorkArea.mostra_workarea(self.SCREEN)
                        self.objPalette.mostra_palette(self.SCREEN)
                        pygame.display.update()

    def botoes_Tela(self, temp):
        if temp == 0:
            posx = self.objWorkArea.retorna_posx()
            self.objWorkArea.modifica_posx(posx - 50)
            print "Diminui posx"
            self.objWorkArea.mostra_workarea(self.SCREEN)
            self.objPalette.mostra_palette(self.SCREEN)
            pygame.display.update()
        elif temp == 1:
            posx = self.objWorkArea.retorna_posx()
            self.objWorkArea.modifica_posx(posx + 50)
            print "Aumenta posx"
            self.objWorkArea.mostra_workarea(self.SCREEN)
            self.objPalette.mostra_palette(self.SCREEN)
            pygame.display.update()

        elif temp == 2:
            if self.file.askOpenOk() == 1:
                programa = self.file.openFile()
                self.objWorkArea.recria_programa(programa)
                self.objWorkArea.mostra_workarea(self.SCREEN)
                self.objPalette.mostra_palette(self.SCREEN)
                pygame.display.update()
                #Gera apartir do texto o programa

        elif temp == 3:
            text = self.objWorkArea.gera_programa()
            print text

            self.file.saveFile(text)

        elif temp == 4:
            #Enviar arquivo
            teste = self.objSerial.localiza_arduino()
            if teste == 0:
                pass
                #Pega os dados e envia
            else:
                pass
                #Mostra uma msg na tela demonstrando qual foi o ocorrido
            pass

