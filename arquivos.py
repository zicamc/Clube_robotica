#-*- coding: utf-8 -*-

#Classe responsavel por salvar e abrir os arquivos
import Tkinter
import tkFileDialog
import tkMessageBox

class Arquivos():

    def __init(self):
        #self.textOpen = //Opções para ingles ou portugues
        #self.textSave = //Opcoes para ingles ou portugues
        pass

    def openFile(self):

        root = Tkinter.Tk()
        file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Escolha o arquivo', initialdir='prog/', filetypes=[('Programa de envio para o arduino','*.pard')])

        if file != None:
            data = file.read()
            file.close()
            print "I got %d bytes from this file." % len(data)
            root.wm_withdraw()
            return data

        root.wm_withdraw()
    
    def saveFile(self,texto):
        root = Tkinter.Tk()
        fileName = tkFileDialog.asksaveasfilename(parent=root,initialdir='prog/',filetypes=[('Programa de envio para o arduino','*.pard')] ,title="Save the image as...")

        if len(fileName ) > 0:
            print "Now saving under %s" % fileName
            file = open(fileName,"w")
            file.write(texto)
            file.close()

        root.wm_withdraw()

    def askOpenOk(self):
        root = Tkinter.Tk()
        teste = tkMessageBox.askyesno(parent=root,title='ALERTA ALERTA ALERTA', message='Se voce abrir um arquivo, voce poderá perder a presente programação:')
        root.wm_withdraw()

        if teste:
            return 1
        return 0