from PySimpleGUI import Frame, Text, Button, Window, WINDOW_CLOSED
def popup_correct_answer(player):
    frame_layout = [[ Text('GREAT!! THE QUESTION IS CORRECT',  background_color='#86dff5', text_color='black')],
                    [ Text(f'THE {player}  EARNED A POINT',  background_color='#86dff5', text_color='black')],
                    [ Text('+1 point', background_color='#86dff5', text_color='black')],]

    layout = [[ Frame('r', layout=frame_layout, background_color='#86dff5', element_justification='c')],
              [ Button('CLOSE',  button_color=('black', '#86dff5'))]]
    
    window =  Window('GREAT!!', layout, element_justification='c', background_color='white')

    while True:
        print(window)
        event, value = window.read()

        if event ==  WINDOW_CLOSED or event == 'CLOSE':
            window.close()
            break


def popup_incorrect_answer(question):
    error_color = "#f79393"
    frame_layout = [[ Text('OH NO!! THE QUESTION IS INCORRECT',  background_color=error_color, text_color='black')],
                    [ Text(f'THE CORRECT ANSWER IS: ',  background_color=error_color, text_color='black')],
                    [ Text(f'->{question["correct_answer"]}<-'.upper(), background_color=error_color, text_color='black')],]

    layout = [[ Frame('r', layout=frame_layout, background_color=error_color, element_justification='c')],
              [ Button('CLOSE',  button_color=('black', error_color))]]
    
    window =  Window('OH NO!!', layout, element_justification='c', background_color='white')

    while True:
        print(window)
        event, value = window.read()
        
        if event ==  WINDOW_CLOSED or event == 'CLOSE':
            window.close()
            break






if __name__ == '__main__':
    questao = {'title':'What is the capital of France?', 
                'alternatives':['Berlin', 'Madrid', 'Paris', 'Rome'],
                'correct_answer':'Paris'}
    
    popup_incorrect_answer(questao)