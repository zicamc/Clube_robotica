# -*- coding: utf-8 -*-
# To change this template, choose Tools | Templates
# and open the template in the editor.

import pygame
from imagens import Imagem_palette

class Palette(object):
    def __init__(self):
        #Inicia os rects da área
        self.lista_palette = []

        #Criando palette azul
        self.imgPalette = Imagem_palette("Imagens/Palette/back_azul.gif","Imagens/aba_azul.gif",(620,9))
        self.imgPalette.add_botao("Imagens/tempo.gif","Imagens/delay.gif",(661,31),0)
        self.imgPalette.add_botao("Imagens/botao_motor.gif","Imagens/Motor.gif",(661,128),1)
        self.imgPalette.add_botao("Imagens/botao_LED.gif","Imagens/LED.gif",(661,217),2)
        self.lista_palette.append(self.imgPalette)

        #Criando palette vermelha
        self.imgPalette = Imagem_palette("Imagens/Palette/back_vermelho.gif","Imagens/aba_vermelha.gif",(621,144))
        self.lista_palette.append(self.imgPalette)

        self.imgPalette = 0

        self.troca_palette = 0
        self.seleciona_caixa = 0

    def mostra_palette(self,SCREEN):
        for i in range(len(self.lista_palette)):
            self.lista_palette[i].show_aba(SCREEN)
            
        self.lista_palette[self.troca_palette].show_palette(SCREEN)
        pygame.display.update((620,0,180,600))

    def verifica_palette(self, posicao):
        if ( posicao[0] < 650 ):
            for i in range(len(self.lista_palette)):
                if ( self.lista_palette[i].colide_aba(posicao) == 1):
                    self.troca_palette = i
                    return 1 #Troca de palette
            return 0

        else:
            return self.lista_palette[self.troca_palette].colide_botao(posicao)
