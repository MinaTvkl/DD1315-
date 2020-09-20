import random
import text_encryption_function #importerar kryoteringsfunktionen
'''Uppgift 1'''

def copy_text_file(in_file, out_file):
    fr = open(in_file, 'r') #öppnar filen så att den går att läsa
    text = fr.read() #variabel som innehåller filens innehåll
    fr.close()
    fw = open(out_file, 'w') #öppnar filen så att den går att skriva i
    fw.write(text) #klisrar in in_files innehåll i out_file
    fw.close()
#copy_text_file("namn.csv", "my_copy.csv")

'''Uppgift 2'''

def encrypt_file(in_file, out_file):
    fr = open(in_file, 'r')
    text = fr.read()
    fr.close()
    encrypted_text = text_encryption_function.encrypt(text) #texten krypteras och sätts in i en variabel
    fw = open(out_file, 'w')
    fw.write(encrypted_text) #den krypterade texten klistras in i en ny fil
    fw.close()

#encrypt_file("namn.csv", "secret_names.csv")

'''Uppgift 3: Skapa en funktion user_dialogue() som ber om namn på två filer,
och kör er egen funktion encrypt_file (från Uppgift 2) på dessa två filer. Er nya funktion (user_dialogue) skall ha felhantering,
och fånga upp om in_file inte existerar, och i sådana fall fråga efter ett nytt filnamn. '''
def user_dialogue():
    file_exists = False
    out_file = input("Name of the new encrypted file: ")
    while not file_exists: #loopar ifall in filen inte finns
        try:
            in_file = input("Name of the file to be encrypted: ")
            encrypt_file(in_file, out_file) #testar kryptera
        except FileNotFoundError:
            print("File or directory does not exist, try again: ")
        else:
            file_exists = True #hoppar ur loopen om filen finns
            print("Encryption completed!")
#user_dialogue()

'''Uppgift 4'''

def get_int_input(prompt_string):
    integer = False
    while not integer:
        try:
            user_in = input(prompt_string)
            int_user_in = int(user_in)
        except ValueError:
            print("You did not enter an integer, try again")
        else:
            integer = True
            return(int_user_in)
#get_int_input("Enter an integer: ")
'''Uppgift 5'''
short_quiz_list_of_lists = [['Vad heter Norges huvudstad?', 'Oslo', 'Bergen', 'Köpenhamn'],
                            ['Vad står ABBA för?', 'Agneta Björn Benny Annefrid', 'Kalle och Lisa', 'Smarrig Sill']]
number_of_questions = len(short_quiz_list_of_lists)
correct_answers = 0
for i in range(0, number_of_questions):
    print(short_quiz_list_of_lists[i][0],
          "Alternativ 1:", short_quiz_list_of_lists[i][1],
          "Alternativ 2:", short_quiz_list_of_lists[i][2],
          "Alternativ 1:", short_quiz_list_of_lists[i][3])
    quiz_answ = get_int_input("Vilket är ditt svar? (1, 2, 3) ")
    if quiz_answ == 1:
        print("Rätt svar!")
        correct_answers += 1
    else:
        print("Fel svar!")
print("Antal rätt: ", correct_answers, "/", number_of_questions)

'''Uppgift 6'''
#string.strip() #tar bort skräptecken
#string.split(";") #delar upp en sträng till en lista vid semikolon ;
def get_quiz_list_handle_exceptions():
    # sätter upp boolian för att senare ta mig vidare efter test
    file_format_and_exsist_test = False
    in_file = input("Skriv in quiz filnamn:")  # här är filnamnet som ska testas
    while not file_format_and_exsist_test:
        # testar
        try:
            fr = open(in_file, "r")  #testar att öppna filen
        except FileNotFoundError:  #om filen inte existerar ger den en output
            print("Filen existerar inte!")
            in_file = input("Skriv in ett nytt quiz filnamn: (glöm ej format) ")
        else:
            for line in fr:  #testar så att varje rad följr formatet!
                file_count = line.count(";") #funktion som räknar antalet semikolon på varje rad
                if file_count == 3: #om det finns 4 listplatser
                    file_format_and_exsist_test = True
                else:
                    in_file = input("Filens format är fel! Du kan behöva kolla så att filen följer rätt protokoll! \n" "Skriv in en ny fil: ")
                    fr.close()
                    break

    fr = open(in_file, "r")

    list2 = [] #huvudlistan
    for line in fr:  # går igenom filen rad för rad
        de_junked = line.strip('\n')  #tar bor \n
        list1 = de_junked.split(';') #gör en lista vid ;
        list2.append(list1)  #lägg till listan av fråga och svar i en position av listan som innehåller alla
    fr.close()
    return list2
#get_quiz_list_handle_exceptions() test för uppg. 6

#Uppgift 7
print('''----------------------------------------
Hello and welcome to the quiz!
----------------------------------------''')
quiz_list = get_quiz_list_handle_exceptions()
number_of_questions = len(quiz_list)
correct_answers = 0
for i in range(0, number_of_questions):
    print(quiz_list[i][0],
          "Alternativ 1:", quiz_list[i][1],
          "Alternativ 2:", quiz_list[i][2],
          "Alternativ 3:", quiz_list[i][3])
    quiz_answer = get_int_input("Vilket är ditt svar? (1, 2, 3) ")
    if quiz_answer == 1:
        print("Rätt svar!")
        correct_answers += 1
    else:
        print("Fel svar!")
print("Antal rätt: ", correct_answers, "/", number_of_questions)

















