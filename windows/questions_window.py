from PySimpleGUI import Text, Button, Window, WINDOW_CLOSED
from windows.popups import popup_correct_answer, popup_incorrect_answer

def questions_window(question, player, theme, points):
    letters = ['A', 'B', 'C', 'D']
    layout = [[ Button(f'{player}   |   Points: {points}'.upper(), size=(30, 3),button_color=('black', 'white'), disabled=True)],
              [ Text('', background_color=theme['background'])],
              [ Text('', background_color=theme['background'])],
              [ Text(f'{question["title"].split()[0:7]}'.upper().replace("'","").replace('[','').replace(']','').replace(',',''), background_color=theme['background'], text_color=theme['text-color'])],
              [ Text(f'{question["title"].split()[7:]}'.upper().replace("'","").replace('[','').replace(']','').replace(',',''), background_color=theme['background'], text_color=theme['text-color'])],              
              [ Text('', background_color=theme['background'])],
              [[ Button(f'{letters[counter]} - {alternative}'.upper(), 
                        size=(40, 3), key=f'{alternative}', button_color=theme['background-button']
                        )] 
                        for counter, alternative in enumerate(question['alternatives'])],
              ]
    

    window =  Window('THE KNOW-IT-ALL', 
                       layout=layout, 
                       element_justification='c', 
                       background_color=theme['background'],
                       size=(400, 450) )

   
    
    while True:
        event, value = window.read()

        if event== WINDOW_CLOSED or event=='Exit':
            raise()


        if event.upper().strip() == question['correct_answer'].upper().strip():
            popup_correct_answer(player)
            window.close()
            return 1

        else:
            popup_incorrect_answer(question)
            window.close()
            return 0




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



