import subprocess
import os



class convert():
    def __init__(self):
        self.arq = '/home/lenovo-tikal2/Desktop/pdfzao.pdf'




    def _converter(self, arquivo = None):

        input1 = self.arq
        output = '/home/lenovo-tikal2/Desktop/cover.txt'
        os.system(("pdftotext %s %s") %( input1, output))

x = convert()

#try:
#    nome_arquivo = input('Nome do arquivo a ser editado:')
#    arquivo = open(nome_arquivo, 'r+')
#except FileNotFoundError:
#    arquivo = open(nome_arquivo, 'w+')
#    arquivo.writelines(u'Arquivo criado pois nao existia')
##faca o que quiser
#arquivo.close()
