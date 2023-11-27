from PySimpleGUI import Text, Button, Window, WINDOW_CLOSED
def message_window():

    layout = [[ Text('PLAYER 1 AND PLAYER 2 GET', background_color='white', text_color='black')],
              [ Text('READY !', background_color='white', text_color='black')],
              [ Text('EACH QUESTION WILL BE', background_color='white', text_color='black')],
              [ Text('WORTH 1 POINT.', background_color='white', text_color='black')],
              [ Text('WAIT EVERYONE`S TURN.', background_color='white', text_color='black')],
              [ Text('GOOD LUCK!', background_color='white', text_color='black')],
              [ Text('BECAUSE YOU WILL NEED IT ...', background_color='white', text_color='black')],
              [ Text('', background_color='white')],
              [ Text('', background_color='white')],
              [ Button('LET`S GO!!!', key='start', button_color='#00B2FF')]
            ]

    window =  Window('THE KNOW-IT-ALL', 
                       layout=layout, element_justification='c',  
                       background_color='white',
                       size=(300, 270))

    while True:
        event, value = window.read()
        
        if event ==  WINDOW_CLOSED:
            window.close()
            break

        if event == 'start':
            window.close()
            return True

if __name__ == "__main__":
    None
