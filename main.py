from threading import Thread
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from lib.colorConvert import ColorConvert
from lib.serialControler import SerialControler

Window.size = (720,360)

class ScreenManagement(ScreenManager):
    pass

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        self.bgcolor= (55 / 255.0), (93 / 255.0), (121 / 255.0)
        self.serial = SerialControler()
        self.color= ColorConvert()
        Clock.schedule_interval(self.updateScreen, 0.1)
        super(HomeScreen, self).__init__(**kwargs)
    def updateScreen(self,*kwargs):
        try:
            if (self.serial.conectado == False):
                self.serial.conect()
            self.th = Thread(target=self.serial.leitura())
            self.th.start()

            if (self.serial.dados != None):
                material = str(self.color.getNome(self.serial.dados))
                # print('Cor: ' + material + ' valor: ' + str(self.serial.dados))
                self.ids.btnColor.color = self.serial.dados[0] / 255, self.serial.dados[1] / 255, self.serial.dados[2] / 255, 1
                self.ids.lbText.text = 'Eu posso ver, é um objeto de cor ' + material + ' e codigo rgb: ' + str(self.serial.dados)
                self.ids.imagem.source = 'img/2.png'
        except Exception as erro:
            self.ids.imagem.source = 'img/3.png'
            self.ids.lbText.text = 'Erro: '+ str(erro)

tela = Builder.load_file("tela.kv")

class MainApp(App):

    def build(self):
        self.title = 'Identificador de cores'

        return tela

if __name__ == "__main__":
    MainApp().run()