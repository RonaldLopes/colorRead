import serial
import time

class SerialControler():

    def __init__(self):
        self.address = None
        self.baudRate = 1200
        self.serial = None
        self.conectado = False
        self.dados=None

    def conect(self, address="/dev/ttyACM0", baudRate='9600'):

        if self.conectado == False:
            try:
                self.address = address
                self.baudRate = baudRate
                self.serial = serial.Serial(address, str(baudRate),timeout=0)
                self.conectado = True
            except Exception as erro:
                print("Erro ao Conectar: "+str(erro))
        else:
            try:
                self.serial.close()
                self.conectado = False
            except:
                pass

    def leitura(self):  # iniciar contabilização
        if self.conectado != False:
            try:
                pacote = self.serial.readline()
                data_str = pacote.decode('ascii')
                pacote = None
                # time.sleep(0.5)
                self.serial.flush()
                self.dados= self.convertToRGBValue(data_str)
            except:
                pass
    def convertToRGBValue(self, text=''):
        if(text.find(',')>=0):
            r,g,b = text.replace('\r\n','').replace('(','').replace(')','').split(',')
            return (int(r),int(g),int(b))
        else:
            return None
