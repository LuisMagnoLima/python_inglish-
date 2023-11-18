import PySimpleGUI as sg

layout = [
    [sg.Button('Left Aligned', button_color=('white', 'black'), key='button1')],
    [sg.Button('Center Aligned', key='button2')],
    [sg.Button('Right Aligned', button_color=('white', 'black'), key='button3')],
    [sg.Button('Exit')]
]

window = sg.Window('Button Text Alignment Example', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

window.close()