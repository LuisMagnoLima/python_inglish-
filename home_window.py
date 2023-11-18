from message_window import message_window
import PySimpleGUI as sg

def start_window():
    layout = [[sg.Image('imagens/imagem1.png')],
              [sg.Text('', background_color='white')],
              [sg.Button('START', size=(10, 1), button_color='#00B2FF')],
              [sg.Button('EXIT', size=(10, 1), button_color='#BE0303')],
            ]

    window = sg.Window('Select the players names', layout=layout, element_justification='c',  background_color='white')

    while True:
        event, value = window.read()
        print(event)
        if event == sg.WINDOW_CLOSED or event == 'EXIT':
            break
        elif event=='START':
            window.close()
            return True


if __name__ == "__main__":
    None