# -*- coding: utf-8 -*-
import pygame
import pygame.font
from configuracoes import config_caixa
from configuracoes import all_config
from caixa import caixa
pygame.font.init()

#===============================================================================
#                   CAIXA INICIO
#===============================================================================
class caixa_inicio(caixa):
    def __init__(self):
        """

        """
        caixa.__init__(self)
        self.posicao = (20, int(all_config.data["altura_caixas"]))
        self.imagem = pygame.image.load("Imagens/Inicio.gif").convert()

        fonte = pygame.font.Font("comic.ttf", config_caixa.data['caixa_inicio'][self.lingua]['tamanho'])
        texto = fonte.render(config_caixa.data['caixa_inicio'][self.lingua]['texto'], True, (0, 0, 0))
        pos = eval(config_caixa.data['caixa_inicio'][self.lingua]['pos'])
        self.imagem.blit(texto,pos)
        self.imagem = pygame.transform.rotate(self.imagem,90)
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