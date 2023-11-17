import PySimpleGUI as sg
def questions_window(question):
    letters = ['A', 'B', 'C', 'D']
    layout = [[sg.Text(f'{player}'), sg.Text(f'Pontos: {pontos}')],
              [sg.Text(question['title'])],
              [[sg.Radio(f'{letters[counter]}', group_id='alternatives', size=(2,2), key=f'{alternative}'), 
                sg.Text(f'{alternative}', size=(20, 1))] for counter, alternative in enumerate(question['alternatives'])],
              [sg.Button('Confirm', size=(8)), sg.Button('Exit', size=(8))],
              ]
    
    window = sg.Window('Menu players', layout=layout, element_justification='c')

    while True:
        event, value = window.read()
        print(event, value)
        if event==sg.WINDOW_CLOSED or event=='Exit':
            break


if __name__=="__main__":
    questao = {'title':'description of the question', 
               'alternatives':['answer 1', 'answer 2fgohgoifhegoh wogji oweirjgojewrgo ijreg', 'answer 3', 'answer 4'],
               'correct_answer':'awnser 1'}
    
    questions_window(questao)