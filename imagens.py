# -*- coding: utf-8 -*-
# To change this template, choose Tools | Templates
# and open the template in the editor.

import pygame
import pygame.font
from caixas.configuracoes import config_botoes
from caixas.configuracoes import all_config

pygame.font.init()

class Image(object):
    def __init__(self, image, pos):
        print image, pos
        self.image = pygame.image.load(image)
        self.image.convert()
        self.pos = pos
        self.rect_image = 0
        self.text = 0

    def show(self,screen):
        self.rect_image = screen.blit(self.image, self.pos)

    def colide(self,posicao):
        return self.rect_image.collidepoint(posicao)

    def show_em_nova_posicao(self,screen, posicao):
        self.pos = posicao
        self.rect_image = screen.blit(self.image, posicao)

    def add_text(self,ID):
        print "entrei"

class RetanguloP(object):
    """
    Aqui estão todas os métodos nessesários para o uso da palette
    """
    def __init__(self,imagem, caixa, posicao, ID):
        """
        Está é o método que tem todos as váriaveis de um "retangulo que possui mtas formas,
        no caso da
        """
        self.ID = ID
        self.pos = posicao
        self.image = Image(imagem,posicao)
        if ID == 12:
            print "entrando"
            self.image.add_text(ID)
       
        self.caixa = Image(caixa,(800,600))
        
    def colide_rect(self, pos):
        """
        Retorna o rect, para verificar se ocorreu a colisão
        """
        return self.image.colide(pos)

    def show_ID(self):
        """
        """
        return self.ID

    def show_image(self,screen):
        """
        Está será a função que irá trocar a palette, eu acho
        """
        self.image.show(screen)
        lingua = all_config.data['lingua']
        fonte = pygame.font.Font("comic.ttf", config_botoes.data[self.ID][lingua]['tamanho'])
        text = fonte.render(config_botoes.data[self.ID][all_config.data['lingua']]['texto'] , True, (0, 0, 0))
        screen.blit(text,( self.pos[0] + 68 - text.get_width()/2 , self.pos[1] + 28 - text.get_height()/2 ))

    def return_caixa(self):
        """
        Está função retornará o ID de caixa
        """
        return self.caixa

    def return_ID(self):
        """
        Oi
        """
        return self.ID

class Imagem_palette(object):
    """

    """
    def __init__(self,imagem_palette, imagem_aba, posicao_aba):
        """
        Esta funcao guarda as imagens e os botões da palette
        """
        #Guarda a imagem da palette
        self.imagem_palette = Image(imagem_palette,(650,0))
        #Guarda a posicao inicial e a imagem da aba para testar a colisao
        self.imagem_aba =  Image(imagem_aba, posicao_aba)

        self.lista_botoes = 0
        self.imagem_botao = []

    def show_palette(self,SCREEN):
        self.imagem_aba.show(SCREEN)
        self.imagem_palette.show(SCREEN)
        
        for i in range(len(self.imagem_botao)):
            self.imagem_botao[i].show_image(SCREEN)
        
        pygame.display.update((620,0,180,600))
        return 0

    def show_aba(self,SCREEN):
        self.imagem_aba.show(SCREEN)

    def colide_aba(self, posicao):
        return self.imagem_aba.colide(posicao)
        
    def colide_botao(self, posicao):
        for i in range(len(self.imagem_botao)):
            if( self.imagem_botao[i].colide_rect(posicao) == 1):
                return (self.imagem_botao[i].return_caixa(), self.imagem_botao[i].return_ID())

        return 0

    def add_botao(self, imagem_botao, caixa, posicao, ID):
        self.imagem_botao.append(RetanguloP(imagem_botao,caixa,posicao, ID))
        