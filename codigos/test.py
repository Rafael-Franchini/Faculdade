import PySimpleGUI as sg

class telapython:
    def __init__(self):
        #layout
        layout =(
            [sg.Text('calculadora')],
            [sg.Text('A'),sg.Input(size=(5,0))],
            [sg.Text('B'),sg.Input(size=(5,0))],
            [sg.Text('C'),sg.Input(size=(5,0))],
            [sg.Button('calcular')]
        )
        #janela
        janela=sg.Window("dados da conta").layout(layout)
        #extrair dados da tela
        self.button, self.values = janela.read()
    def iniciar(self):
        print(self.values)
        A=self.values['A']
        B=self.values['B']
        C=self.values['C']
tela = telapython()
tela.iniciar()