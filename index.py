from home_window import start_window
from message_window import message_window
from questions_window import questions_window

if __name__ == "__main__":

    # vars
    theme1 = {'background': 'white', 'text-color': 'black', 'background-button': '#53079F'}
    theme2 = {'background': 'white', 'text-color': 'black', 'background-button': '#b30036'}
    player1 = 'Jogador 1'
    player2 = 'Jogador 2'
    questao = {'title':'What is the capital of France?', 
               'alternatives':['Berlin', 'Madrid', 'Paris', 'Rome'],
               'correct_answer':'awnser 1'}

    
    # begin code
    start = start_window()
    if start:
        message_window()
        questions_window(player=player1, question=questao, theme=theme1, points=0)



