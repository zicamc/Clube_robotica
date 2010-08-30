# -*- coding: utf-8 -*-
# To change this template, choose Tools | Templates
# and open the template in the editor.
import serial
import os

class Serial_Arduino():

    def __init__(self):

        self.port_arduino = 0

    def localiza_arduino(self):
        SISTEMA_OPERACIONAL = os.uname()[3]
        if SISTEMA_OPERACIONAL.find("Ubuntu") > 0:
            i = 0
            while i < 5:
                print "Tentando"
                try:
                    port = '/dev/ttyUSB'+chr(i+48)
                    print port
                    self.port_arduino = serial.Serial( port ,9600)
                    self.port_arduino.timeout = 10
                    print "Consegui a serial"
                    print self.port_arduino.open()
                    print self.port_arduino.write(chr(254))
                    print "Resposta"
                    teste = self.port_arduino.read()
                    print teste
                    if teste == chr(48):
                        print "Este é o arduino mesmo"
                    else:
                        print teste
                        print "desculpa mas este não é o arduino"
                    self.port_arduino.close()
                    break

                except:
                    i += 1;
                    print "sem serial"

            return -1

    def envia(self, programa):
        pass
    
