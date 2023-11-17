

import PySimpleGUI as sg

def window_names():

    layout = [[sg.Text('**PLAYER** 1 AND PLAYER 2 GET READY !*', background_color='white', text_color='black')],
              [sg.Text('READY !', background_color='white', text_color='black')],
              [sg.Text('EACH QUESTION WILL BE WORTH 1 POINT.', background_color='white', text_color='black')],
              [sg.Text('WORTH 1 POINT.', background_color='white', text_color='black')],
              [sg.Text('WAIT EVERYONE’S TURN.', background_color='white', text_color='black')],
              [sg.Text('GOOD LUCK!', background_color='white', text_color='black')],
              [sg.Text('BECAUSE YOU WILL NEED IT ...', background_color='white', text_color='black')],
            ]

    window = sg.Window('Select the players names', layout=layout, element_justification='c',  background_color='white')

    while True:
        event, value = window.read()
        print(event)
        if event == sg.WINDOW_CLOSED or event == 'EXIT':
            break


if __name__ == "__main__":
    window_names()