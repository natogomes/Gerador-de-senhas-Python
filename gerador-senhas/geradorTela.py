import PySimpleGUI as sg
import random, string

sg.theme('darkBlack1')
layout = [
    [sg.Image('tituloGerador.png', pad=(0, (0, 10)))],
    [sg.Text('Tamanho da senha (Dígitos): ', font='Heveltica, 15'),
     sg.Input(size=(3, 1), font='Heveltica, 15', key='tamanho')],
    [sg.Text('Digite os Símbolos e Caracteres opcionais:', font='Heveltica, 15', pad=(0, (10, 0)))],
    [sg.Input(font='Heveltica 15', key='simbol', size=(39, 1), pad=(0, (0, 10)))],
    [sg.Text('Senha', font='Heveltica 15')],
    [sg.InputText(size=(25, 1), font='Arial, 28', pad=(0, (0, 10)), key='saida')],
    [sg.Button('GERAR', size=(8, 1), font='Arial 12'), sg.Button('Sair', size=(8, 1), font='Arial 12')]
]
tela = sg.Window('SafePassword', element_justification='center', layout=layout,
                 size=(500, 315), finalize=True)
simbolos = ''
while True:
    event, values = tela.read()
    if event == sg.WIN_CLOSED:
        break

    if values['simbol'] == '':
        simbolos = '@!#"$%¨&*()_+:><;?/`´^~'
    else:
        simbolos = values['simbol']

    if event == 'GERAR' and values['tamanho'] == '':
        sg.popup('Informe o tamanho da senha!')
        continue

    elif event == 'GERAR':
        carac = string.ascii_letters + string.digits + simbolos
        sisran = random.SystemRandom()
        tela['saida'].update(''.join(sisran.choice(carac) for i in range(int(values['tamanho']))))

    elif event == 'Sair':
        break

