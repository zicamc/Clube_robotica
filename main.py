# -*- coding: utf-8 -*-
# To change this template, choose Tools | Templates
# and open the template in the editor.
__author__="zeck"

import pygame
import sys
from Tela import tela

#Declarando variáveis do ambiente
CLOCK = pygame.time.Clock()

#Métodos
def treat_events():
    """
    Função que verifica se algo aconteceu para que o programa se feche.
    """
    # Criar uma thread para isso
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                                           sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:     sys.exit()

#Inicia pygame e a tela


pygame.init()
screen = tela()
screen.inicia_screen()

#Iniciando o programa em si
while 1:
    CLOCK.tick(5)
    screen.acoes()
    treat_events()
    