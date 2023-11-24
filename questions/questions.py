import pickle

def creating_questions():

    questions = [
        {'title': 'What is the biggest planet of our system?', 'alternatives': ['Earth', 'Jupiter', 'Mars', 'Saturn'], 'correct_answer': 'Jupiter', 'index': '0'},

        {'title': 'Who was the first Brazillian president?', 'alternatives': ['Getúlio Vargas', 'Marechal Deodoro da Fonseca', 'Juscelino Kubitschek', 'Tancredo Neves'], 'correct_answer': 'Marechal Deodoro da Fonseca', 'index': '1'},

        {'title': 'What year was assigned the Declaration of Independence of USA?', 'alternatives': ['1776', '1789', '1804', '1812'], 'correct_answer': '1776', 'index': '2'},

        {'title': 'What is the square root of 144?', 'alternatives': ['10', '12', '14', '16'], 'correct_answer': '12', 'index': '3'},

        {'title': 'Who wrote it Dom Quixote?', 'alternatives': ['William Shakespeare', 'Miguel de Cervantes', 'Dante Alighieri', 'Jane Austen'], 'correct_answer': 'Miguel de Cervantes', 'index': '4'},

        {'title': 'What is the longest river in the world?', 'alternatives': ['Mississipi', 'Nilo', 'Yangtzé', 'Amazonas'], 'correct_answer': 'Amazonas', 'index': '5'},

        {'title': 'What is the atomic number of oxygen?', 'alternatives': ['6', '8', '14', '16'], 'correct_answer': '8', 'index': '6'},

        {'title': 'Who painted the Mona Lisa?', 'alternatives': ['Pablo Picasso', 'Vincent Van Gogh', 'Leonardo da Vinci', 'Michelangelo'], 'correct_answer': 'Leonardo da Vinci', 'index': '7'},

        {'title': 'What year occured the French Revolution?', 'alternatives': ['1668', '1776', '1789', '1815'], 'correct_answer': '1789', 'index': '8'},

        {'title': 'Who was the leader of the Cuban Revolution in 1959?', 'alternatives': ['Fidel Castro', 'Che Guevara', 'Fulgencio Batista', 'Camílio Cienfuegos'], 'correct_answer': 'Fidel Castro', 'index': '9'},

        {'title': 'What is the most populated country?', 'alternatives': ['India', 'China', 'USA', 'Brazil'], 'correct_answer': 'China', 'index': '10'},

        {'title': 'Who is the author of Theory of Relativity?', 'alternatives': ['Isaac Newton', 'Galileu Galilei', 'Albert Einstein', 'Stephen Hawking'], 'correct_answer': 'Albert Einstein', 'index': '11'},

        {'title': 'What is the largest desert of the world', 'alternatives': ['Saara', 'Gobi', 'Atacama', 'Antártica'], 'correct_answer': 'Antártica', 'index': '12'},

        {'title': 'Who discorvered penicillin', 'alternatives': ['Alexander Fleming', 'Marie Curie', 'Louis Pasteur', 'Jonas Salk'], 'correct_answer': 'Alexander Fleming', 'index': '13'},

        {'title': 'What is the most abundant element in Earth Surface?', 'alternatives': ['Ferro', 'Silício', 'Oxigênio', 'Alumínio'], 'correct_answer': 'Oxigênio', 'index': '14'},

        {'title': 'Who was the first man to step on the moon', 'alternatives': ['Yuri Gargarin', 'Neil Armstrong', 'Buzz Aldrin', 'Michael Collins'], 'correct_answer': 'Neil Armstrong', 'index': '15'},

        {'title': 'What is the WWFs symbol animal?', 'alternatives': ['Tigre', 'Elefante', 'Panda', 'Gorila'], 'correct_answer': 'Panda', 'index': '16'},

        {'title': 'Who wrote it Romeu and Julieta?', 'alternatives': ['Charles Dickens', 'William Faulkner', 'William Shakespeare', 'Ziraldo'], 'correct_answer': 'William Shakespeare', 'index': '17'},

        {'title': 'What is the capital city of Canada?', 'alternatives': ['Vancouver', 'Toronto', 'Montreal', 'Ottawa'], 'correct_answer': 'Ottawa', 'index': '18'},

        {'title': 'How many continents exist?', 'alternatives': ['5', '6', '7', '8'], 'correct_answer': '6', 'index': '19'},

        {'title': 'what is the chemical formula of water?', 'alternatives': ['CO2', 'O2', 'CH4', 'H20'], 'correct_answer': 'H20', 'index': '20'},

        {'title': 'Who was the inventor of the telephone?', 'alternatives': ['Alexander Graham Bell', 'Nikola Tesla', 'Thomas Edison', 'Marconi'], 'correct_answer': 'Alexander Graham Bell', 'index': '21'},

        {'title': 'What is the second largest ocean in the world?', 'alternatives': ['Oceano Índico', 'Oceano Atlântico', 'Oceano Antártico', 'Oceano Pacífico'], 'correct_answer': 'Oceano Atlântico', 'index': '22'},

        {'title': 'Who was the founder of Microsoft?', 'alternatives': ['Steve Jobs', 'Bill Gates', 'Mark Zuckerberg', 'Jeff Bezos'], 'correct_answer': 'Bill Gates', 'index': '23'},

        {'title': 'In what year did the First World War start?', 'alternatives': ['1905', '1923', '1939', '1914'], 'correct_answer': '1914', 'index': '24'},

        {'title': 'What country is known as the "Land of the Rising Sun?', 'alternatives': ['China', 'Japan', 'India', 'Australia'], 'correct_answer': 'Japan', 'index': '25'},

        {'title': 'Who was the creator of the company Apple?', 'alternatives': ['Steve Wozniak', 'Tim Cook', 'Steve Jobs', 'Bill Gates'], 'correct_answer': 'Steve Jobs', 'index': '26'},

        {'title': 'What is the biggest land mammal?', 'alternatives': ['Elephant', 'Giraffe', 'Rhinoceros', 'Blue Whale'], 'correct_answer': 'Elephant', 'index': '27'},

        {'title': 'Who was the South African leader that fought against apartheid?', 'alternatives': ['Nelson Mandela', 'Desmond tutu', 'F.W. de Klerk', 'Thabo Mbeki'], 'correct_answer': 'Nelson Mandela', 'index': '28'},

        {'title': 'What is the biggest animal on the planet?', 'alternatives': ['Elephant', 'Giraffe', 'Rhinoceros', 'Blue Whale'], 'correct_answer': 'Blue Whale', 'index': '29'},

        {'title': 'Who was the first Roman emperor?', 'alternatives': ['Julio Caesar', 'Augustus', 'Nero', 'Trajan'], 'correct_answer': 'Augustus', 'index': '30'},

        {'title': 'What is the largest lake in the world by volume of water?', 'alternatives': ['Lake Victoria', 'Lake Baikal', 'Lake Superior', 'Lake Titicaca'], 'correct_answer': 'Lake Baikal', 'index': '31'},

        {'title': 'Who is the author of "The Little Prince"?', 'alternatives': ['J.K. Rowling', 'Antoine de Saint-Exupéry', 'Roald Dahl', 'CS Lewis'], 'correct_answer': 'Antoine de Saint-Exupéry', 'index': '32'},

        {'title': 'What is the capital of Australia?', 'alternatives': ['Sydney', 'Melbourne', 'Canberra', 'Brisbane'], 'correct_answer': 'Canberra', 'index': '33'},

        {'title': 'Who was the painter of the works The Starry Night and sunflowers?', 'alternatives': ['Pablo Picasso', 'Claude Monet', 'Vincet Van Gogh', 'Salvador Dalí'], 'correct_answer': 'Vincent Van Gogh', 'index': '34'},

        {'title': 'What is the fifth planet in the solar system?', 'alternatives': ['Mars', 'Jupiter', 'saturn', 'Uranus'], 'correct_answer': 'Jupiter', 'index': '35'},

        {'title': 'Who was the leader of the Bolshevik Revolution in Russia?', 'alternatives': ['Vladimir Lenin', 'José Stalin', 'Leon Trotsky', 'Mikhai Gorbachevl'], 'correct_answer': 'Vladimir Lenin', 'index': '36'},

        {'title': 'What is the only metal that is liquid at room temperature?', 'alternatives': ['Gold', 'Lead', 'Mercury', 'Iron'], 'correct_answer': 'Mercury', 'index': '37'},

        {'title': 'Who was the creator of the theory of species evolution?', 'alternatives': ['Charles Darwin', 'Gregor Mendel', 'Alfred Russel Wallace', 'Thomas Huxely'], 'correct_answer': 'Charles Darwin', 'index': '38'},

        {'title': "What is the world's largest coffee producer?", 'alternatives': ['Brazil', 'Colombia', 'Vietnam', 'Ethiopia'], 'correct_answer': 'Brazil', 'index': '39'},

        {'title': 'Who was the first astronaut to orbit the Earth?', 'alternatives': ['Yuri Gagarin', 'Alan Shepard', 'John Glenn', 'Neil Armstrong'], 'correct_answer': 'Yuri Gagarin', 'index': '40'},

        {'title': 'What is the full name of the physicist known as Hawking?', 'alternatives': ['Stephen Alexander Hawking', 'tephen William Hawking', 'Stephen James Hawking', 'Stephen Richard Hawking'], 'correct_answer': 'Stephen William Hawking', 'index': '41'},

        {'title': 'Who was the author of "The Three Musketeers"?', 'alternatives': ['Victor hugo', 'Alexandrdre Dumas', 'Gustave Flaubert', 'Émile Zola'], 'correct_answer': 'Alexandre Dumas', 'index': '42'},

        {'title': 'In what year was the UN (United Nations) founded?', 'alternatives': ['1945', '1950', '1960', '1975'], 'correct_answer': '1945', 'index': '43'},

        {'title': 'hat is the second largest country in the world by land area?', 'alternatives': ['China', 'United States', 'Russia', 'Canada'], 'correct_answer': 'Rússia', 'index': '44'},

        {'title': 'Who was the Greek philosopher known for his contributions to ethics?', 'alternatives': ['Plato', 'Aristotle', 'Socrates', 'Epicurus'], 'correct_answer': 'Aristotle', 'index': '45'},

        {'title': 'at is the most abundant element in the human body?', 'alternatives': ['iron', 'Oxygen', 'Carbon', 'Calcium'], 'correct_answer': 'Oxygen', 'index': '46'},

        {'title': 'Who is known as "the Bard of Avon"?', 'alternatives': ['William Wordsworth', 'Jhon Milton', 'William Shaekespeare', 'Geoffrey Chaucer'], 'correct_answer': 'William Shaekespeare', 'index': '47'},

        {'title': 'What is the only planet in the solar system that rotates clockwise?', 'alternatives': ['Venus', 'Uranus', 'Neptune', 'Mars'], 'correct_answer': 'Venus', 'index': '48'},]


    with open('questions.pickle', 'wb') as file:
        pickle.dump(questions, file)


def reading_questions():
    with open('questions.pickle', 'rb') as file:
        questions = pickle.load(file)
        return questions


def remove_question(question_to_remove):
    questions = []
    questions_with_filter = []

    # reading questions
    with open('questions.pickle', 'rb') as file:
        questions = pickle.load(file)
        print(f'temos {len(questions)} questoes')

    # filter question selected
    for question in questions:
        if not question_to_remove['index'] == question['index']:
            questions_with_filter.append(question)
     
    # saving questions in file
    with open('questions.pickle', 'wb') as file:
        pickle.dump(questions_with_filter, file)





if '__main__' == __name__:
    creating_questions()
    questions = reading_questions()
    remove_question(questions[22])
    questions = reading_questions()

    for question in questions:
       print(f'{question},\n')

    
   