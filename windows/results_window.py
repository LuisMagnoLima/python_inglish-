from PySimpleGUI import Image, Text, Button, Window, WINDOW_CLOSED


def victory_player(player, points, theme):
    layout = [[ Text(f'CONGRATULATION, THE -> {player} <- IS THE CHAMPION!!!'.upper(), 
                       background_color=theme['background'],
                       text_color=theme['text-color'])],

              [ Text(f'HE SCORED {points} POINTS!!!!', 
                       background_color=theme['background'],
                       text_color=theme['text-color'])],

              [ Button('CLOSE', button_color=theme['background-button'])]
              ]

    window =  Window('WINNER', 
                       layout, 
                       element_justification='center',
                       background_color=theme['background'])

    while True:
        event, value = window.read()
        if event ==  WINDOW_CLOSED or event == 'CLOSE':
            window.close()
            break

def draw(theme, points):
    layout = [[ Text(f'the match is over and we have a draw!'.upper(), 
                       background_color=theme['background'],
                       text_color=theme['text-color'])],

              [ Text(f'both players scored {points} points'.upper(), 
                       background_color=theme['background'],
                       text_color=theme['text-color'])],

              [ Button('CLOSE', button_color=theme['background-button'])]
              ]
    

    window =  Window('WINNER', 
                       layout, 
                       element_justification='center',
                       background_color=theme['background'])

    while True:
        event, value = window.read()
        if event ==  WINDOW_CLOSED or event == 'CLOSE':
            window.close()
            break
    



if __name__ == '__main__':
    theme2 = {'background': 'white', 'text-color': 'black', 'background-button': '#b30036'}
    victory_player('player 3', 30, theme2)
    draw(theme2,40)