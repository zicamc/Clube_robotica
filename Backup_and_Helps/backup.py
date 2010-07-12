# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import pygame.font 
import easygui
import Palette

global PROGRAMACAO, indice_PROGRAMACAO
indice_PROGRAMACAO = 0

class Palette(): #Classe da Palette

    def __init__(self,screen):                          #Inicia a classe Palette
        global palette, ID_GUIA, w                                  #Define como global as variaveis palette(imagem da pallette) e ID_GUIA(identificador da guia/aba)
        self.screen = screen                                        #Atribuição de variaveis
        self.palette_1   = pygame.image.load("Imagens/Palette/back1.gif")   #Carrega a imagem back1.gif para a variavel palette_1
        self.palette_2   = pygame.image.load("Imagens/Palette/back2.gif")   #Carrega a imagem back2.gif para a variavel palette_2
        self.palette_3   = pygame.image.load("Imagens/Palette/back3.gif")   #Carrega a imagem back3.gif para a variavel palette_3
        self.palette_4   = pygame.image.load("Imagens/Palette/back4.gif")   #Carrega a imagem back4.gif para a variavel palette_4
        self.palette_5   = pygame.image.load("Imagens/Palette/back5.gif")   #Carrega a imagem back5.gif para a variavel palette_5
        self.palette = self.palette_4                              #Define que a primeira palette é a da variavel palette_1
        ID_GUIA = 1                                                 #Atribui valor 1 a variavel ID_GUIA, demonstrando que a é a primeira PALETTE que tá na tela
        
    def Print_Palette(self):                 #Inicia a definção/função que imprime a palette
        self.screen.blit(self.palette,(620,0))    #Joga a o primeiro pixel da imagem que está na variavel palette na poição do pixel 620,0


    def Swap_Palette(self,mouse_y):   #Definição/Função de troca de ABAS da PALETTE
        if mouse_y > 10 and mouse_y < 138: # Se o clique do mouse foi na posição y entre 10 e 138 é para trocar para a primeira palette
            self.palette = self.palette_1         #palette recebe a imagem de palette_1
            ID_GUIA = 1                           #Atribui valor 1 a variavel ID_GUIA, demonstrando que a é a primeira PALETTE que tá na tela
                    
        elif mouse_y > 145 and mouse_y < 273: #Se o clique do mouse foi entre 145 e 273 é pra trocar pra segunda palette
            self.palette = self.palette_2         #a variavel palette recebe a imagem da variavel palette_2
            ID_GUIA = 2                           #Atribui valor 2 a variavel ID_GUIA, demonstrando que a é a segunda PALETTE que tá na tela

        elif mouse_y > 278 and mouse_y < 407: #Se o clique do mouse foi entre 278 e 407 éé pra trocar pra terceira palette
            self.palette = self.palette_3         #a variavel palette recebe a imagem da variavel palette_3
            ID_GUIA = 3                           #Atribui valor 3 a variavel ID_GUIA, demonstrando que a é a terceira PALETTE que tá na tela

        elif mouse_y > 413 and mouse_y < 514: #Se o clique do mouse foi entre 413 e 514 é para trocar para a quarta palette
            self.palette = self.palette_4         #a variavel palette recebe a imagem da variavel palette_4
            ID_GUIA = 4                           #Atribui valor 4 a variavel ID_GUIA, demonstrando que a é a quarta PALETTE que tá na tela

        elif mouse_y > 519 and mouse_y < 600: #Se o clique do mouse foi entre 519 e 600 é para trocar para a quinta palette
            self.palette = self.palette_5         #a variavel palette recebe a imagem da variavel palette_5
            ID_GUIA = 5                           #Atribui valor 1 a variavel ID_GUIA, demonstrando que a é a QUINTA PALETTE que tá na tela


    def Verifica_toque(self,pos):              #Função que verifica o toque na Palette
        COLOR_PALETTE = screen.get_at((750,2))      #Pega a cor da palette, existem 5 palettes, com 5 cores diferentes
        if COLOR_PALETTE == (0,0,255,255):          #Verifica se a cor é azul  
            print 'oi'
            
        elif COLOR_PALETTE == (255,0,0,255):        #Verifica se a cor é vermelha
            print '2 - motor 1'
            
        elif COLOR_PALETTE == (128,128,0,255):      #Verifica se a cor é Verde musgo
            print '3 - motor 1'
            
        elif COLOR_PALETTE == (0,128,0,255):        #Verifica se a cor é verde forte
            if pos[0] > 680 and pos[0] < 790:
                if pos[1]>30 and pos[1] < 90:
                    return 1

                elif pos[1]> 100 and  pos[1]<200:
                    return 2

                elif pos[1]> 210 and  pos[1]<310:
                    return 3

                elif pos[1]>325 and pos[1]<425:
                    return 4

                else:
                    return None

        else:                                       #Verifica se a cor é bege
            print '5 - motor 1'

class Work_Area():                               #Classe da "Area de trabalho"'

    def __init__(self):                                #Inicia a classe Work_Area
        global screen, background, MOUSE_IMAGE                #Define como global as variaveis screen e background
        global CENTRO_IMAGEM                                  #Esta variavel vai demonstrar aonde está o centro dá ultima figura da programação, seja uma caixa vazia ou não
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Interface")               #Define que o nome da janela
        background = pygame.Surface((800,600))                #Define que a variavel background é uma Surface do tamanho da tela.
        background = background.convert()                     #Background é convertida de simples pixels para uma "imagem" 
                                                              #A 'imagem' background será o lugar que todas as 'imagens' serão colocadas
        background.fill((100,255,0))
        CENTRO_IMAGEM = (160,220)                             #MOSTRA AONDE ESTÀ O CENTRO DA PRIMEIRA CAIXA VAZIA

        pygame.font.init()                                    #inicia uma classe da biblioteca pygame responsável pelas fontes de escrita do programa
        self.fonte = pygame.font.Font("comic.ttf",30)

        #IMAGENS DA PROGRAMAÇÃO
        self.INICIO         = pygame.image.load("Imagens/Inicio.gif")
        self.CAIXA_VAZIA    = pygame.image.load("Imagens/Caixa.gif")
        self.MOUSE_IMAGE    = pygame.image.load("Imagens/one_pixel.gif")
        self.DELAY          = pygame.image.load("Imagens/delay.gif")
        self.ACENDE_LED     = pygame.image.load("Imagens/Acende_Led.gif")
        self.APAGA_LED      = pygame.image.load("Imagens/Apaga_Led.gif")
        self.ESPERA_TOQUE   = pygame.image.load("Imagens/Toque.gif")

    def init_Background(self):
        global CENTRO_IMAGEM
        #Imprime a imagem do 'INICIO' da programação
        background.blit (self.INICIO, (20,170))
        #As duas linhas abaixo cria uma reta e um triangulo, fazendo parecer uma SETA
        pygame.draw.line(background, (0,0,0),(70,220),(90,220),20)
        pygame.draw.polygon(background,(0,0,0), ( (90,200) ,(90,240),(110,220)))
        #Imprime uma CAIXA_VAZIA
        background.blit(self.CAIXA_VAZIA, (110,170))
        CENTRO_IMAGEM = (160,220)                             #MOSTRA AONDE ESTÀ O CENTRO DA PRIMEIRA CAIXA VAZIA

    def Print_Work_Area(self,POSICAO_X):           #Definição ou função para imprimir a "Area de trabalho"
        screen.blit(background, (0 - POSICAO_X ,0))       #A função screen.blit joga na tela a "imagem" que foi criada na função de inicialização na posição (0,0)
                                                          #para iniciar o programa. A variavel da posição X da tela é incrementada para que haja uma amplitude maior de programação visual


    def Print_Background(self,pos):               #Função que irá adicionar as imagens no Background :P
        global CENTRO_IMAGEM
        if abs(pos[0]-CENTRO_IMAGEM[0]) <= 50 and abs(pos[1]-CENTRO_IMAGEM[1]) <= 50:
            background.blit(self.MOUSE_IMAGE,(CENTRO_IMAGEM[0]-50,CENTRO_IMAGEM[1]-50))
            cor_imagem = self.MOUSE_IMAGE.get_at((93,93))

##            if cor_imagem == (5,251,92,255):
##                tempo = easygui.enterbox("Escreva o tempo de espera, em segundos:\n\t\tExemplo:  3.4","Tempo de Espera(NÂO FINALIZADO)") 
##                #Verifica se houve alguma entrada de dados
##                while tempo == "":
##                    tempo = easygui.enterbox("Escreva o tempo de espera, em segundos:\n\t\tExemplo:  3.4","Tempo de Espera") 
##                texto = self.fonte.render(tempo+" s",True,(0,0,0))
##                #Imprime o tempo na tela
##                background.blit(texto,(CENTRO_IMAGEM[0]-40,CENTRO_IMAGEM[1]-10))

            if cor_imagem == (255,0,0,255):
                led = easygui.buttonbox("Escreva o led que vai acende","SELECAO DE LEDS acender(NAO FINALIZADO)",("1","2","3","1 e 2","1 e 3","2 e 3","1,2 e 3"))
                texto = self.fonte.render(led,True,(0,0,0))
                #Imprime o tempo na tela
                if led == "1" or led == "2" or led == "3":
                    background.blit(texto,(CENTRO_IMAGEM[0]-10,CENTRO_IMAGEM[1]))
                elif led == "1 e 2" or led == "1 e 3" or led == "2 e 3":
                    background.blit(texto,(CENTRO_IMAGEM[0]-40,CENTRO_IMAGEM[1]))
                else:
                    self.fonte = pygame.font.Font("comic.ttf",20)
                    texto = self.fonte.render(led,True,(0,0,0))
                    background.blit(texto,(CENTRO_IMAGEM[0]-35,CENTRO_IMAGEM[1]+10))
                    self.fonte = pygame.font.Font("comic.ttf",30)
                
            elif cor_imagem == (255,0,1,255):
                led = easygui.buttonbox("Escreva o led que vai apagar","SELECAO DE LEDS apagar(NAO FINALIZADO)",("1","2","3","1 e 2","1 e 3","2 e 3","1,2 e 3")) 
                texto = self.fonte.render(led,True,(0,0,0))
                #Imprime o tempo na tela
                if led == "1" or led == "2" or led == "3":
                    background.blit(texto,(CENTRO_IMAGEM[0]-10,CENTRO_IMAGEM[1]))
                elif led == "1 e 2" or led == "1 e 3" or led == "2 e 3":
                    background.blit(texto,(CENTRO_IMAGEM[0]-40,CENTRO_IMAGEM[1]))
                else:
                    self.fonte = pygame.font.Font("comic.ttf",20)
                    texto = self.fonte.render(led,True,(0,0,0))
                    background.blit(texto,(CENTRO_IMAGEM[0]-35,CENTRO_IMAGEM[1])+10)
                    self.fonte = pygame.font.Font("comic.ttf",30)
                
            elif cor_imagem == (255,255,0,255):
                toque = easygui.buttonbox("Escolha entre as tres opções!\nEspera toque ...","Escolha Toque",("Esquerda","Direita","Esquerda e Direita"))
                if toque == "Esquerda":
                    self.fonte = pygame.font.Font("comic.ttf",20)
                    texto = self.fonte.render(toque,True,(0,0,0))
                    #Imprime o tempo na tela
                    background.blit(texto,(CENTRO_IMAGEM[0]-42,CENTRO_IMAGEM[1]))
                    self.fonte = pygame.font.Font("comic.ttf",30)

                elif toque == "Direita":
                    self.fonte = pygame.font.Font("comic.ttf",20)
                    texto = self.fonte.render(toque,True,(0,0,0))
                    #Imprime o tempo na tela
                    background.blit(texto,(CENTRO_IMAGEM[0]-35,CENTRO_IMAGEM[1]))
                    self.fonte = pygame.font.Font("comic.ttf",30)

                else:
                    self.fonte = pygame.font.Font("comic.ttf",15)
                    texto = self.fonte.render("Esq. e Dir.",True,(0,0,0))
                    #Imprime o tempo na tela
                    background.blit(texto,(CENTRO_IMAGEM[0]-40,CENTRO_IMAGEM[1]+5))
                    self.fonte = pygame.font.Font("comic.ttf",30)
                    

    def Print_Background_NEW(self):
        #Imprime a proxima seta e caixa:
        pygame.draw.line(background, (0,0,0),(CENTRO_IMAGEM[0]+50,220),(CENTRO_IMAGEM[0]+70,220),20)
        pygame.draw.polygon(background,(0,0,0), ( (CENTRO_IMAGEM[0]+70,200) ,(CENTRO_IMAGEM[0]+70,240),(CENTRO_IMAGEM[0]+90,220)))
        CENTRO_IMAGEM = (CENTRO_IMAGEM[0] + 140,CENTRO_IMAGEM[1])
        background.blit(self.CAIXA_VAZIA, (CENTRO_IMAGEM[0]-50,170))
    
    def Mouse_Print(self,pos):
        screen.blit(self.MOUSE_IMAGE, pos)         #'imprime' em cima da screen o ponteiro do mouse junto com a imagem

    def swap_MOUSE_IMAGE(self,ID):
        if ID == 1:    #ID 1 significa que é um delay, espera
            self.MOUSE_IMAGE = self.DELAY

        elif ID == 2:  #ID 2 significa que é uma estrutura para acender led
            self.MOUSE_IMAGE = self.ACENDE_LED

        elif ID == 3:
            self.MOUSE_IMAGE = self.APAGA_LED
        
        elif ID == 4:
            self.MOUSE_IMAGE = self.ESPERA_TOQUE
        else:
            print "OI"

           
def main():       #Função Main
    
    try:
        import psyco
        psyco.full()
    except ImportError:
        pass

    pygame.mixer.pre_init(44100,-16,2, 1024)
    pygame.init()                 #Incia o módulo pygame.

    #INICIALIZAÇÃO DOS OBJETOS UTILIZADOS NO PROGRAMA.
    w = Work_Area()               #atribui a w a Classe Work_Area, isso faz com que a classe seja incializada
    p = Palette.Palette(screen)           #atribui a p a Classe Palette, enviando como referencia a variavel screen, que veio incializada como global da classe Work_Area()
    w.init_Background()
    
    # INICIALIZAÇÃO DE VARIAVEIS, COM SEUS RESPECTIVOS VALORES
    mouse_pos = (0,0)
    POSICAO_X = 0
    MOUSE_PRESS = False

    while True:
        
        for event in pygame.event.get():

            if event.type == MOUSEBUTTONDOWN:     #Verifica se o evento foi do clique de um botão no mouse
                    mouse_pos = event.pos               #Guarda a posição do mouse na hora do evento
                    if event.button == 1:                     #Verifica se foi o botão da direita que foi clicado
                        
                        if mouse_pos[0] >= 0 and mouse_pos[0] <=10:     #Verifica se a posição do mouse está entre 0 e 10px no eixo X
                            if POSICAO_X > 0:                               #Verifica se a variavel POSICAO_X é maior do que 0, para que a imagem de fundo não deixe um espaço em branco
                                POSICAO_X -= 30                                 #Faz com que a imagem de fundo ande 10px para esquerda

                        elif mouse_pos[0] >= 610 and mouse_pos[0] <= 620:    #Verifica se a posição do mouse está entre a posição 610 e 620px do eixo y
                            if POSICAO_X < 180:                                  #Verifica se a variavel POSICAO_X é menor que 420, para que a imagem de fundo não deixe um espaço em branco no canto direito
                                POSICAO_X += 30                                  #Faz com que a imagem de fundo ande 10px para direita
                                
                        elif mouse_pos[0] > 620 and mouse_pos[0] < 650:      #Verifica se a posição do mouse no eixo X fica entre 620 e 650
                            p.Swap_Palette(mouse_pos[1])                         #Chama a função Swap_Palette que nada mais é que a troca da imagem da palette, enviando como argumento a posição do mouse no eixo y.
                        
                        elif mouse_pos[0] > 650:                             #Verifica se a posição do mouse era maior que 650 na tela
                            valor = p.Verifica_toque(mouse_pos)                  #Chama a função que verifica aonde foi o toque e que por sua vez retorna um valor
                            w.swap_MOUSE_IMAGE(valor)
                            MOUSE_PRESS = True                                   #Atribui o valor True para a variavel MOUSE_PRES
                            
                    elif event.button == 3:                   #Verifica se o botão do mouse clicado é o botão direito
                        if mouse_pos[0] < 620:                          #Verifica se o toque do botão foi menor que 620
                            print 'delete'                                      #Apenas escreve delete 

            elif MOUSE_PRESS == True:                         #Verifica se a variavel MOUSE_PRESS é verdadeira, para que haja a impressão da imagem junto ao mouse
                if pygame.mouse.get_pressed()[0] == 1:                  #Verifica se o botão do Mouse ainda está precionad
                    w.Mouse_Print(pygame.mouse.get_pos())               #Chama a função que imprime a imagem junto ao ponteiro do mouse a imagem            
                
                else:                                         #Se entra no esle significa que o botão foi 'desclicado'
                    w.Mouse_Print((1000,0))                         #Imprime a imagem que vai junto do mouse num lugar que não se é possivel ver
                    w.Print_Background(pygame.mouse.get_pos())
                    MOUSE_PRESS = False                             #Atribui False ao MOUSE_PRESS
            
            elif event.type == pygame.QUIT:                   #Verifica se o botão de Fechar foi clicado
                pygame.quit()                                           #Finaliza o pygame

            elif event.type == KEYDOWN:   #Verifica se alguma tecla foi clicada
                if event.key == K_ESCAPE:       #Verifica se essa tecla é a de ESCAPE
                    pygame.quit()                   #Finaliza o pygame
                
            
            pygame.display.update()
            w.Print_Work_Area(POSICAO_X)
            p.Print_Palette()
            
if __name__ == '__main__': 
    main()
