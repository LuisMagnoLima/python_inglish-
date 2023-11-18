import PySimpleGUI as sg
def questions_window(question, player, theme, points):
    sg.theme = theme
    letters = ['A', 'B', 'C', 'D']
    layout = [[sg.Button(f'{player}   |   Points: {points}'.upper(), size=(30, 3),button_color=('black', 'white'))],
              [sg.Text('', background_color=theme['background'])],
              [sg.Text('', background_color=theme['background'])],
              [sg.Text(f'{question["title"]}'.upper(), background_color=theme['background'], text_color=theme['text-color'])],
              [sg.Text('', background_color=theme['background'])],
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

        print(event.split()[0].upper())
        print(question['correct_answer'].upper())
        if event==sg.WINDOW_CLOSED or event=='Exit':
            break


        if event.split()[0].upper() == question['correct_answer'].upper():
            # adicionar popup de acerto
            return 1
        
        else:
            # adicionar popup de erro
            return -1




if __name__=="__main__":

    # vars
    theme1 = {'background': 'white', 'text-color': 'black', 'background-button': '#53079F'}
    theme2 = {'background': 'white', 'text-color': 'black', 'background-button': '#b30036'}
    player1 = 'Jogador 1'
    player2 = 'Jogador 2'
    questao = {'title':'What is the capital of France?', 
               'alternatives':['Berlin', 'Madrid', 'Paris', 'Rome'],
               'correct_answer':'Paris'}

    
    questions_window(player=player1, question=questao, theme=theme1, points=0)



