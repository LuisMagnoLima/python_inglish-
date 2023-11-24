import PySimpleGUI as sg
def message_window():

    layout = [[sg.Text('PLAYER 1 AND PLAYER 2 GET', background_color='white', text_color='black')],
              [sg.Text('READY !', background_color='white', text_color='black')],
              [sg.Text('EACH QUESTION WILL BE', background_color='white', text_color='black')],
              [sg.Text('WORTH 1 POINT.', background_color='white', text_color='black')],
              [sg.Text('WAIT EVERYONE`S TURN.', background_color='white', text_color='black')],
              [sg.Text('GOOD LUCK!', background_color='white', text_color='black')],
              [sg.Text('BECAUSE YOU WILL NEED IT ...', background_color='white', text_color='black')],
              [sg.Text('', background_color='white')],
              [sg.Text('', background_color='white')],
              [sg.Button('LET`S GO!!!', key='start', button_color='#00B2FF')]
            ]

    window = sg.Window('Select the players names', 
                       layout=layout, element_justification='c',  
                       background_color='white',
                       size=(300, 270))

    while True:
        event, value = window.read()
        
        if event == sg.WINDOW_CLOSED:
            window.close()
            break

        if event == 'start':
            window.close()
            return True

if __name__ == "__main__":
    None
