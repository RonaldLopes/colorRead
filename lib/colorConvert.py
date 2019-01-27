'''
Desenvolvido por Ronald Lopes
Versão: 1.0
Data: 19/01/2019

Descrição:
    Esta classe serve para retornar o nome de uma cor a partir de seu valor em RGB, caso o valor não seja um valor padrão a classe retorna a cor mais aproximada.
'''

class ColorConvert(object):
    def __init__(self):
        try:
            import webcolors
            self.biblioteca= webcolors
        except:
            print('Tentando adicionar as bibliotecas necessárias...')
            try:
                import os
                os.system('pip install webcolors')
                import webcolors
                self.biblioteca = webcolors
            except Exception as erro:
                print('Não foi possivel iniciar a classe: '+erro)
                exit()

    def corAproximada(self,corRequerida):
        '''Retorna no nome da cor mais semelhante a buscada, para isso é efetuado um erro medio quadratico e o q tiver o menor erro se torna o mais proximo'''
        coresAnalizadas={}
        for key, nome in self.biblioteca.css3_hex_to_names.items():
            corAtualR, corAtualG,corAtualB = self.biblioteca.hex_to_rgb(key)
            diferencaR = corAtualR-corRequerida[0]
            diferencaG = corAtualG-corRequerida[1]
            diferencaB = corAtualB-corRequerida[2]
            erroMedioTotal = (diferencaR**2) + (diferencaG**2) + (diferencaB**2)
            coresAnalizadas[erroMedioTotal] = nome
        return coresAnalizadas[min(coresAnalizadas.keys())]

    def getNome(self, corRGB):
        try:
            return self.biblioteca.rgb_to_name(corRGB)
        except:
            print('Buscando Cor mais proxima...')
            return self.corAproximada(corRequerida=corRGB)

    def getHexCode(self, rgb):
        return self.biblioteca.rgb_to_hex(rgb)

    def getHexCodeNormalize(self,rgb):
        return self.biblioteca.name_to_hex(self.getNome(rgb))
