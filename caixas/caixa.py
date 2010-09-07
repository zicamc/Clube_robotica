# -*- coding: utf-8 -*-

import sys
from configuracoes import all_config
import pygame
import pygame.font

pygame.font.init()
fonte = pygame.font.Font("comic.ttf", 25)

class caixa():
    def __init__(self):
        self.lingua = all_config.data['lingua']

        self.posicao = (0, 0)
        self.rect = 0
        self.selecao_visivel = True

        self.prog_text = ""
        self.prog_arduino = ""
        self.CLOCK = pygame.time.Clock()

    def troca_posicao(self, posicao):
        self.posicao = posicao

    def colide(self, pos):
        try:
            return self.rect.collidepoint(pos)
        except:
            return 0

    def retorna_pos(self):
        return self.posicao

    def retorna_texto(self):
        return self.prog_text

    def retorna_prog(self):
        return self.prog_arduino
    
    def gera_texto(self):
        pass

    def treat_events(self):
        """
        Função que verifica se algo aconteceu para que o programa se feche. Aqui por preguica, nao tava afim de faze um import!
        """
        # Criar uma thread para isso
        for event in pygame.event.get():
            if event.type == pygame.QUIT:                                           sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:     sys.exit()

    def teclado_numerico(self,key):
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