import PySimpleGUI as sg
def questions_window(question, player, theme, points):
    sg.theme = theme
    letters = ['A', 'B', 'C', 'D']
    layout = [[sg.Text(f'{player}'.upper(), size=(10, 3), background_color='white', text_color='black'), 
               sg.Text(f'Points: {points}', size=(10, 3), background_color='white', text_color='black')],
              [sg.Text(f'{question["title"]}'.upper(), background_color='white', text_color='black')],
              [[sg.Button(f'{letters[counter]} - {alternative}'.upper(), 
                        size=(40, 3),
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
    
    theme1 = {'background': 'white', 'text-color': 'black', 'background-button': 'blue'}

    theme2 = {'background': 'white', 'text-color': 'black', 'background-button': 'red'}
    
    player = 'Jogador1'

    points = 0

    questions_window(questao, player, theme1, points)