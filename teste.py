import PySimpleGUI as sg

texto_longo = "Texto longo que você deseja quebrar automaticamente em duas linhas"

layout = [
    [sg.Button('', key='botao', button_color=('white', sg.theme_background_color())),
     sg.Text(texto_longo, size=(15, 2), justification='left')],
    [sg.Button('OK'), sg.Button('Cancelar')]
]

window = sg.Window('Botão com Texto quebrado', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break

window.close()