"""
Av: Mina Tavakoli
Uppgift: 178 Periodiska systemet
17 april 2017
"""

from random import choice
from operator import attrgetter
import os


class Atom:
    """ Klass för alla atomer som läses in från textfilen
    """
    def __init__(self, symbol, number, weight):
        """ Skapar en ny atom
        """
        self.symbol = symbol  # Sträng med atombeteckning
        self.weight = weight  # Decimaltal som står för atomvikten
        self.number = number  # Heltal som står för atomnummer

    def __str__(self):
        """ Avgör hur atombeteckning, atomnummer och atomvikt framförs i listan av atomer
        """
        return '\nAtombeteckning: {}\nAtomnummer: {}\nAtomvikt: {}\n'.format(self.symbol, self.number, self.weight)

    def __repr__(self):
        """ Returnerar objektens attribut på strängform
        """
        return str(self)


def atom_list():
    """ Läser in textfilen, skapar objekt för atomerna & returnerar dessa i en lista
    """
    atomlist = []
    fr = open('atoms.txt', 'r')
    number = 0  # Atomerna tilldelas startnummer, de tilldelas rätta nummer i funktionen sort_atoms
    for line in fr:
        split_list = line.split(' ')
        if split_list[1] == '':
            weight = split_list[2].rstrip()
        else:
            weight = split_list[1].rstrip()
        symbol = split_list[0]
        atom = Atom(symbol, int(number), float(weight))
        atomlist.append(atom)
    fr.close()
    return atomlist


def sort_atoms(atomlist):
    """ Sorterar listan efter vikt, tilldelar atomernas atomnummer, byter plats på lämpliga atomer och
     sorterar igen efter atomnummer
     """
    sorted_list = sorted(atomlist, key=attrgetter('weight'))
    sorted_list[17], sorted_list[18] = sorted_list[18], sorted_list[17]
    sorted_list[26], sorted_list[27] = sorted_list[26], sorted_list[27]
    sorted_list[51], sorted_list[52] = sorted_list[52], sorted_list[51]
    sorted_list[89], sorted_list[90] = sorted_list[90], sorted_list[89]
    sorted_list[91], sorted_list[92] = sorted_list[92], sorted_list[91]
    i = 0
    for atom in sorted_list:
        i += 1
        atom.number = i
    sorted_list = sorted(sorted_list, key=attrgetter('number'))
    return sorted_list


def lower_menu():
    """ Meny som kallas på efter varje quiz, läster in användarval och felhanterar
    """
    user_option = 0
    wrong_input = True
    print('\n----------------------------------------------'
          '\n1. Fortsätt träna \n2. Tillbaka till huvudmenyn')
    while wrong_input:
        try:  # Felhantering av användarval
            user_option = int(input('Vad vill du göra? '))
            if user_option == 1 or user_option == 2:
                wrong_input = False
            else:
                raise ValueError
        except ValueError:
            print('Ogiltigt val, välj alternativ 1 eller 2')
    return user_option


def handle_quiz_input(question, guess):
    """Felhantering av svar: undersöker om användarens svar är i rätt format
    indata är användarens svar samt frågan för att bestämma vilken typ av svar som krävs,
    returnerar svaret i rätt format
    """
    guess = guess.replace(' ', '')
    wrong_format = True
    if question == 'Vilket atomnummer har ':
        while wrong_format:
            try:
                int(guess)
            except ValueError:
                guess = input('Svara med ett heltal, försök igen: ')
            else:
                wrong_format = False
    elif question == 'Hur många atomhenheter väger ':
        while wrong_format:
            try:
                guess = guess.replace(',', '.')
                float(guess)
            except ValueError:
                guess = input('Svara med en siffra, försök igen: ')
            else:
                wrong_format = False
    else:
        while not guess.isalpha():
            guess = input('Svara med en text, försök igen: ')
    return guess


def quiz_response(question, question_attr, answer_attr):
    """ Svarsfunktionen: läser in användarens svar till quizarna och rättar,
    indata är frågan som en sträng, attributet som det frågas efter och attributet som är det rätta svaret
    """
    attempt = 3
    while attempt > 0:
        guess = str(input(question + str(question_attr) + '? '))
        guess = handle_quiz_input(question, guess)  # Felhantering av svar
        if guess == str(answer_attr).lower():
            print('Rätt svar!')
            attempt = 0
        else:
            attempt -= 1
            if attempt > 0:
                print('Fel svar, du har ' + str(attempt) + ' försök kvar!')
            else:
                print('Fel svar!\nRätt svar är: ' + str(answer_attr))


def number_quiz(atomlist):
    """ Quiz på atomnummer: indata är atomlistan, slumpar en atom och anropar svarsfunktionen
    """
    run_quiz = True
    while run_quiz:
        rand_atom = choice(atomlist)
        quiz_response('Vilket atomnummer har ', rand_atom.symbol, rand_atom.number)
        user_option = lower_menu()
        if user_option == 2:
            run_quiz = False


def symbol_quiz(atomlist):
    """ Quiz på atombeteckning: indata är atomlistan, slumpar en atom anropar svarsfunktionen
    """
    run_quiz = True
    while run_quiz:
        rand_atom = choice(atomlist)
        quiz_response('Vilken atombeteckning har atomen med atomnumnret ', rand_atom.number, rand_atom.symbol)
        user_option = lower_menu()
        if user_option == 2:
            run_quiz = False


def weight_quiz(atomlist):
    """ Quiz på atomvikt: skapar en lista med tre slumpmässiga atomer och slumpar det rätta svaret samt skriver ut
    de tre atomernas vikt som svarsalternativ, indata är atomlistan
    """
    run_quiz = True
    while run_quiz:
        rand_list = []
        options_list = []
        for i in range(0, 3):
            rand_atom = choice(atomlist)
            options_list.append(rand_atom.weight)
            rand_list.append(rand_atom)
            atomlist.remove(rand_atom)
            i += 1
        correct_answer = choice(rand_list)
        print('\nAlternativ: ' + str(options_list)[1:-1])  # Skriver ut alternativen utan paranteser
        quiz_response('Hur många atomhenheter väger ', correct_answer.symbol, correct_answer.weight)
        # Anropar svarsfunktionen
        user_option = lower_menu()  # Anropar fortsättningsmenyn
        if user_option == 2:
            run_quiz = False


def main_menu(atomlist):
    """ Huvudmenyn: skriver ut menyn, läser in användarval och felhanterar samt anropar vald quiz, indata är atomlistan
    """
    running = True
    while running:
        os.system('cls' if os.name == 'nt' else 'clear')  # Tömmer terminalen, OBS! fungerar inte för mac
        print('------------------ MENY --------------------\n'
              '1. Visa alla atomer\n'
              '2. Träna på atomnummer\n'
              '3. Träna på atombeteckningar\n'
              '4. Träna på atomvikt\n'
              '5. Stäng programmet\n'
              '--------------------------------------------')
        wrong_input = True
        user_option = 0
        while wrong_input:
            try:  # Felhantering av användarval
                user_option = int(input('Vad vill du göra? '))
                if 1 <= user_option <= 5:
                    wrong_input = False
                else:
                    raise ValueError
            except ValueError:
                print('Ogiltigt val, välj ett alternativ mellan 1 och 5')
            if user_option == 1:
                print(*atomlist)  # Skriver ut listan med atomer utan kommatecken och paranteser
                input('--------------------------------------------\n'
                      'För att gå tillbaka till menyn, tryck på Retur-tangenten')
            elif user_option == 2:
                number_quiz(atomlist)
            elif user_option == 3:
                symbol_quiz(atomlist)
            elif user_option == 4:
                weight_quiz(atomlist)
            elif user_option == 5:
                running = False


def main():
    """ Programmets "main", alltså huvuddel: anropar de nödvändiga funktioner för att programmet ska köra
    """
    atomlist = sort_atoms(atom_list())  # Skapar den sorterade listan av atomer
    main_menu(atomlist)  # Kör programmet
if __name__ == '__main__':
    main()
