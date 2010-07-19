# -*- coding: utf-8 -*-
import sys
import pygame
import pygame.font
from caixa import caixa
pygame.font.init()
CLOCK = pygame.time.Clock()
fonte = pygame.font.Font("comic.ttf", 25)
#===============================================================================
#                   CAIXA INICIO
#===============================================================================
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

