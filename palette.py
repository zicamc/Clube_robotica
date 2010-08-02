# -*- coding: utf-8 -*-
# To change this template, choose Tools | Templates
# and open the template in the editor.

import pygame
import pygame.font
from imagens import Imagem_palette

class Palette(object):
    """

    """
    def __init__(self):
        """
        """
        #Inicia os rects da área
        self.lista_palette = []

        #Criando palette azul
        self.imgPalette = Imagem_palette("Imagens/Palette/back_azul.gif","Imagens/aba_azul.gif",(620,9))
        self.imgPalette.add_botao("Imagens/tempo.gif","Imagens/delay.gif",(661,31),0)
        self.imgPalette.add_botao("Imagens/botao_motor.gif","Imagens/Motor.gif",(661,128),1)
        self.imgPalette.add_botao("Imagens/botao_LED.gif","Imagens/LED.gif",(661,217),2)
        self.imgPalette.add_botao("Imagens/botao_toque.gif","Imagens/Toque.gif",(661,319),3)
        self.imgPalette.add_botao("Imagens/botao_buzzer.gif","Imagens/buzzer.gif",(661,400),12)     #TODO: ID DO BUZZER é 12

        self.lista_palette.append(self.imgPalette)

        #Criando palette vermelha
        self.imgPalette = Imagem_palette("Imagens/Palette/back_vermelho.gif","Imagens/aba_vermelha.gif",(620,144))
        self.imgPalette.add_botao("Imagens/botao_luz.gif","Imagens/luz.gif",(661,31),10)            #TODO: ID DA LUZ É 10
        self.imgPalette.add_botao("Imagens/botao_temp.gif","Imagens/temperatura.gif",(661,128),11)  #TODO: ID DA Temperatura é 11
        self.lista_palette.append(self.imgPalette)

        self.imgPalette = 0
        self.troca_palette = 0
        self.seleciona_caixa = 0

    def mostra_palette(self,SCREEN):
        """
        """
        for i in range(len(self.lista_palette)):
            self.lista_palette[i].show_aba(SCREEN)
            
        self.lista_palette[self.troca_palette].show_palette(SCREEN)
        pygame.display.update((620,0,180,600))
        #Fim do método
        """"""

    def verifica_palette(self, posicao):
        if ( posicao[0] < 650 ):
            for i in range(len(self.lista_palette)):
                if ( self.lista_palette[i].colide_aba(posicao) == 1):
                    self.troca_palette = i
                    return 1 #Troca de palette
            return 0

        else:
            return self.lista_palette[self.troca_palette].colide_botao(posicao)
