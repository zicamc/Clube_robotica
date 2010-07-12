# -*- coding: utf-8 -*-
# To change this template, choose Tools | Templates
# and open the template in the editor.

import pygame
from imagens import Image
from caixas import *

class Work_Area(object):
    def __init__(self):
        print "Iniciando Work_Area"
        self.posicao_x = 0
        self.posicao_vazia = (120,150)
        self.FUNDO = Image("Imagens/work_area.gif",(0,0))
        self.caixa_vazia = Image("Imagens/Caixa.gif",self.posicao_vazia)
        self.setas = [ Image("Imagens/seta_dir.gif",(590,570)), Image("Imagens/seta_esq.gif",(0,570))]
        self.lista_caixas = [ caixa_inicio() ]

        print "Finalizando Work_Area"

    def mostra_workarea(self,SCREEN):
        print "\t-->  Iniciando show_WorkArea"
        self.caixa_vazia = Image("Imagens/Caixa.gif",(self.posicao_vazia[0]-self.posicao_x,self.posicao_vazia[1]))

        self.FUNDO.show(SCREEN)
        for i in range(len(self.lista_caixas)):
            self.lista_caixas[i].show(SCREEN, self.posicao_x)

        for i in range(len(self.setas)):
            self.setas[i].show(SCREEN)

        self.caixa_vazia.show(SCREEN)
        print "\tFinalizando show_WorkArea <--"

    def nova_caixa(self,SCREEN,posicao, ID_CAIXA):
        """

        """
        if (self.caixa_vazia.colide(posicao) == 1):
            if ID_CAIXA == 0:
                caixa = caixa_tempo()
                caixa.troca_posicao(self.posicao_vazia)
                caixa.events(SCREEN, self.posicao_x)

            self.lista_caixas.append( caixa )
            self.posicao_vazia = (self.posicao_vazia[0]+150, 150)
            self.caixa_vazia = Image("Imagens/Caixa.gif", (self.posicao_vazia[0]-self.posicao_x,self.posicao_vazia[1]))

    def testa_colisao(self,SCREEN,posicao):
        for i in range(len(self.lista_caixas)):
            if (self.lista_caixas[i].colide(posicao) == 1):
                pos_caixa = self.lista_caixas[i].retorna_pos()
                variacao = 0
                if ( pos_caixa[0] - self.posicao_x > 520 or pos_caixa[0] - self.posicao_x < 0):
                    variacao = (pos_caixa[0] - self.posicao_x) - 310
                    self.modifica_posx(self.posicao_x + variacao)
                    self.mostra_workarea(SCREEN)

                pygame.display.update((0,0,620,600))
                self.lista_caixas[i].events(SCREEN, self.posicao_x)
                return 1
        return 0

    def retorna_posx(self):
        return self.posicao_x

    def retorna_posv(self):
        return self.posicao_vazia[0]

    def modifica_posx(self, posicao):
        self.posicao_x = posicao