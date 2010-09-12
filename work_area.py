# -*- coding: utf-8 -*-
# To change this template, choose Tools | Templates
# and open the template in the editor.
import pygame
from imagens import Image
from caixas.caixa_inicio import caixa_inicio
from caixas.caixa_led import caixa_led
from caixas.caixa_luz import caixa_luz
from caixas.caixa_motor import caixa_motor
from caixas.caixa_tempo import caixa_tempo
from caixas.caixa_toque import caixa_toque
from caixas.caixa_temperatura import caixa_temperatura
from caixas.caixa_buzzer import caixa_buzzer
from caixas.configuracoes import all_config

class Work_Area(object):
    def __init__(self):
        """

        """
        print "Iniciando Work_Area"

        pos = eval(all_config.data["tamanho_tela"])

        self.posicao_x = 0
        self.posicao_vazia = (120, int(all_config.data["altura_caixas"]) )
        self.FUNDO = Image("Imagens/work_area.gif",(0,0))
        self.caixa_vazia = Image("Imagens/Caixa.gif",self.posicao_vazia)

        pos = eval(all_config.data["tamanho_tela"])
        posicao_setas = pos[1] - 30
        
        self.setas = [ Image("Imagens/seta_dir.gif",(590,posicao_setas)), Image("Imagens/seta_esq.gif",(0,posicao_setas))]

        posicao_opcoes = pos[1] - 60
        self.opcoes = [ Image("Imagens/abrir.gif",(245, posicao_opcoes)),   Image("Imagens/salvar.gif",(310, posicao_opcoes)),
                        Image("Imagens/enviar.gif",(375, posicao_opcoes))]

        self.lista_caixas = [ caixa_inicio() ]

        print "Finalizando Work_Area"

    def mostra_workarea(self,SCREEN):
        """
        """
        print "\t-->  Iniciando show_WorkArea"
        self.caixa_vazia = Image("Imagens/Caixa.gif",(self.posicao_vazia[0]-self.posicao_x,self.posicao_vazia[1]))

        self.FUNDO.show(SCREEN)
        for i in range(len(self.lista_caixas)):
            self.lista_caixas[i].show(SCREEN, self.posicao_x)

        for i in range(len(self.setas)):
            self.setas[i].show(SCREEN)

        for i in range(len(self.opcoes)):
            self.opcoes[i].show(SCREEN)


        self.caixa_vazia.show(SCREEN)
        print "\tFinalizando show_WorkArea <--"

    def nova_caixa(self,SCREEN,posicao, ID_CAIXA):
        """
        """
        if (self.caixa_vazia.colide(posicao) == 1):
            if ID_CAIXA == 0: #Id do tempo
                caixa = caixa_tempo()
                caixa.troca_posicao(self.posicao_vazia)
                caixa.events(SCREEN, self.posicao_x)

            elif ID_CAIXA == 1: #ID do motor
                caixa = caixa_motor()
                caixa.troca_posicao(self.posicao_vazia)
                caixa.events(SCREEN, self.posicao_x)

            elif ID_CAIXA == 2: #ID do LED
                caixa = caixa_led()
                caixa.troca_posicao(self.posicao_vazia)
                caixa.events(SCREEN, self.posicao_x)

            elif ID_CAIXA == 3: #ID do toque
                caixa = caixa_toque()
                caixa.troca_posicao(self.posicao_vazia)
                caixa.events(SCREEN, self.posicao_x)

            elif ID_CAIXA == 10: #ID da luz
                caixa = caixa_luz()
                caixa.troca_posicao(self.posicao_vazia)
                caixa.events(SCREEN, self.posicao_x)

            elif ID_CAIXA == 11: #ID da temperatura
                caixa = caixa_temperatura()
                caixa.troca_posicao(self.posicao_vazia)
                caixa.events(SCREEN, self.posicao_x)

            elif ID_CAIXA == 12: #ID do buzzer
                caixa = caixa_buzzer()
                caixa.troca_posicao(self.posicao_vazia)
                caixa.events(SCREEN, self.posicao_x)
            
            self.lista_caixas.append( caixa )
            self.posicao_vazia = (self.posicao_vazia[0]+150, self.posicao_vazia[1])
            self.caixa_vazia = Image("Imagens/Caixa.gif", (self.posicao_vazia[0]-self.posicao_x,self.posicao_vazia[1]))
            if ( self.posicao_vazia[0] - self.posicao_x > 500):
                self.posicao_x = self.posicao_x + 300

    def modifica_caixa(self,SCREEN,posicao):
        """

        """
        for i in range(len(self.lista_caixas)):
            if (self.lista_caixas[i].colide(posicao) == 1):
                pos_caixa = self.lista_caixas[i].retorna_pos()
                variacao = 0
                if ( pos_caixa[0] - self.posicao_x > 520 or pos_caixa[0] - self.posicao_x < 0):
                    variacao = (pos_caixa[0] - self.posicao_x) - 310
                    self.modifica_posx(self.posicao_x + variacao)
                    self.mostra_workarea(SCREEN)
                self.lista_caixas[i].events(SCREEN, self.posicao_x)
                return 1
        return 0

    def retira_caixa(self, posicao):
        """
        """
        tamanho = len(self.lista_caixas)
        for i in range(tamanho):
            if self.lista_caixas[i].colide(posicao) == 1:
                self.lista_caixas.pop(i)
                while i < tamanho - 1:
                    pos = self.lista_caixas[i].retorna_pos()
                    self.lista_caixas[i].troca_posicao((pos[0]-150,pos[1]))
                    i = i + 1

                self.posicao_vazia = (self.posicao_vazia[0]-150,self.posicao_vazia[1])
                return 1

        return 0

    def teste_botoes(self, posicao):
        for i in range(len(self.setas)):
            if self.setas[i].colide(posicao) == 1:
                return i
        
        for a in range(len(self.opcoes)):
            if self.opcoes[a].colide(posicao) == 1:
                return a + 2
        
        return -1


    def retorna_posx(self):
        """

        """
        return self.posicao_x

    def retorna_posv(self):
        """

        """
        return self.posicao_vazia[0]

    def modifica_posx(self, posicao):
        """

        """
        if (posicao >= 0):
            self.posicao_x = posicao

    def gera_programa(self):
        texto = ""

        for i in range(len(self.lista_caixas)):
            self.lista_caixas[i].gera_texto()
            texto += self.lista_caixas[i].retorna_texto()
            if i != 0:
                texto += '|'
        return texto

    def recria_programa(self, PROGRAMA):
        self.lista_caixas = [ caixa_inicio() ]
        self.posicao_vazia = (120,150)
        self.posicao_x = 0
        i = PROGRAMA.split('|')
        print i

        for a in range(len(i)-1):
            prog = i[a].split('-')
            print prog
            if (self.recria_caixa(prog[0], prog[1]) != 1):
                print "ERRROOORRRRR"

        print i

        pass

    def recria_caixa(self,ID,PROG):
        print ID,PROG
        print self.lista_caixas

        if ID == '00':
            temp = caixa_tempo()
            temp.recria(self.posicao_vazia, PROG)

        elif ID == '01': #O ID 2 Ficou incluido no LED pro apagar do arduino
            temp = caixa_led()
            temp.recria(self.posicao_vazia, PROG)

        elif ID == '03':
            temp = caixa_motor()
            temp.recria(self.posicao_vazia, PROG)

        elif ID == '04':
            temp = caixa_buzzer()
            temp.recria(self.posicao_vazia, PROG)
       
        elif ID == '05' or ID == '06':
            temp = caixa_toque()
            temp.recria(self.posicao_vazia,ID,PROG)

        elif ID == '07' or ID == '08':
            temp = caixa_temperatura()
            temp.recria(self.posicao_vazia,ID,PROG)
            
        elif ID == '09' or ID == '10':
            temp = caixa_luz()
            temp.recria(self.posicao_vazia,ID,PROG)

        else:
            return 0

        self.lista_caixas.append(temp)
        self.posicao_vazia = (self.posicao_vazia[0] + 150, self.posicao_vazia[1])
        return 1