import PySimpleGUI as sg
def questions_window(question, player, theme, points):
    sg.theme = theme
    letters = ['A', 'B', 'C', 'D']
    layout = [[sg.Button(f'{player}   |   Points: {points}'.upper(), size=(30, 3),button_color=('black', 'white'))],
              [sg.Text(f'{question["title"]}'.upper(), background_color=theme['background'], text_color=theme['text-color'])],
              [[sg.Button(f'{letters[counter]} - {alternative}'.upper(), 
                        size=(40, 3), key=f'{alternative}', button_color=theme['background-button']
                        )] 
                        for counter, alternative in enumerate(question['alternatives'])],
              ]
    

    window = sg.Window('Menu players', 
                       layout=layout, 
                       element_justification='c', 
                       background_color=theme['background'],
                       size=(400, 400) )

    while True:
        event, value = window.read()
        print(event, value)
        if event==sg.WINDOW_CLOSED or event=='Exit':
            break


if __name__=="__main__":


    questao = {'title':'What is the capital of France?', 
               'alternatives':['Berlin', 'Madrid', 'Paris', 'Rome'],
               'correct_answer':'awnser 1'}
    
    theme1 = {'background': 'white', 'text-color': 'black', 'background-button': '#53079F'}

    theme2 = {'background': 'white', 'text-color': 'black', 'background-button': '#b30036'}
    
    player1 = 'Jogador 1'

    player2 = 'Jogador 2'

    points = 0

    questions_window(questao, player1, theme1, points)
    questions_window(questao, player2, theme2, points)