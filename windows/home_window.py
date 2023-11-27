from windows.message_window import message_window
from PySimpleGUI import Image, Text, Button, Window, WINDOW_CLOSED

def start_window():
    layout = [[Image('imagem1.png')],
              [Text('THE KNOW-IT-ALL', background_color='white')],
              [Button('START', size=(10, 1), button_color='#00B2FF')],
              [Button('EXIT', size=(10, 1), button_color='#BE0303')],
            ]

    window =  Window('THE KNOW-IT-ALL', layout=layout, element_justification='c',  background_color='white')

    while True:
        event, value = window.read()
        if event ==  WINDOW_CLOSED or event == 'EXIT':
            break
        elif event=='START':
            window.close()
            return True


if __name__ == "__main__":
    None