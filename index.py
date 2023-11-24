from windows.home_window import start_window
from windows.message_window import message_window
from windows.questions_window import questions_window
from questions import creating_questions, remove_question, reading_questions
from random import randint
from windows.results_window import victory_player, draw

if __name__ == "__main__":
    
    creating_questions()
    questions = reading_questions()
    
    # theme box 
    theme1 = {'background': 'white', 'text-color': 'black', 'background-button': '#53079F'}
    theme2 = {'background': 'white', 'text-color': 'black', 'background-button': '#b30036'}

    # players name
    player1 = 'Player 1'
    player2 = 'Player 2'
    
    player1_score = 0
    player2_score = 0


    # begin code
    start = start_window()
    if start:
        message_window()
     
        try:
            while True:
                # selecting random question
                question = questions[randint(0, len(questions)-1)]    
                # asking to user1 
                player1_score += questions_window(question, player1, theme1, player1_score)
                # removing question of the list
                remove_question(question)
                questions = reading_questions()

                # selecting random question
                question = questions[randint(0, len(questions)-1)]    
                # asking to user2
                player2_score += questions_window(question, player2, theme2, player2_score)
                # removing question of the list
                remove_question(question)
                questions = reading_questions()

                if len(questions) <=2:
                    raise()

        except TypeError as err:

            print(err)


            if player1_score > player2_score:
                victory_player(player1, player1_score, theme1)

            elif player2_score > player1_score:
                victory_player(player2, player2_score, theme2)

            else:
                draw(theme1, player1_score)

        






