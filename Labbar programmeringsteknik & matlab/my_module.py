import csv
#Uppgift 1 Kopieringsprogram

def copy_text_file(in_file, out_file):
    copy_file = open(str(out_file), 'w')
    input_file = open(str(in_file), 'r')
    list_of_input = list(input_file.read())
    for line in list_of_input:
        copy_file.write(line)
    copy_file.close()
    input_file.close()
    returneringstext = "Din fil har kopierats!"
    return returneringstext

#test
#print(copy_text_file("namn.csv", "my_copy.csv"))


#Uppgift 2 Krypteringsprogram

import text_encryption_function

def encrypt_file(in_file, out_file):
    to_be_encrypt = open(str(in_file), 'r')
    to_be_encrypt = to_be_encrypt.read()
    encrypted_file = text_encryption_function.encrypt(to_be_encrypt)
    encrypt = open(str(out_file), 'w')
    encrypt.write(str(encrypted_file))
    encrypt.close()
    returneringstext = "Din fil har krypterats!"
    return returneringstext

#print(str(encrypt_file("namn.csv", "secret_names.csv")))


#Uppgift 3 Kryptering med felhantering
import os

def user_dialogue():
    file_excist = False
    in_file = input("Skriv namn på filen som du vill kryptera: ")
    out_file = input("Skriv namn på filen som du vill ska vara krypterad: ")

    while not file_excist:        #testar
        try:
            encrypt_file(in_file,out_file)
        except FileNotFoundError:
            print("Filen existerar inte!")
            in_file = input("Försök igen: ")
        else:
            file_excist = True
    #while not os.path.isfile(in_file):
    encrypt_your_file = encrypt_file(in_file,out_file)
    print("Din mamma har krypterats! ;) ")

#user_dialogue()

#Uppgift 4 Heltal med felhantering

def get_int_input(prompt_string):
    integer = False
    while not integer:
        try:
            user_in = input(prompt_string) #ifall det inte är  en int
            int_user_in = int(user_in)
        except:
            print("Du gav inte ett heltal!") #så börjar vi om efter som integer inte är True

        else:
            integer = True #Så kommer den avsluta
    return (int_user_in)

#get_int_input("Skriv ett heltal: ")

#Uppgift 5 Ett Quiz-spel

import random

short_quiz_list_of_lists = [
['Vad heter Norges huvudstad?', 'Oslo', 'Bergen', 'Köpenhamn'],
['Vad står ABBA för?', 'Agneta Björn Benny Annefrid', 'Kalle och Lisa', 'Smarrig Sill'],
]

print( "-------------------------------\n Hej och välkommen till quizet!\n-------------------------------")

#fråga 1

print(short_quiz_list_of_lists[0][0])
print("Alternativ 1 = " + short_quiz_list_of_lists[0][1] + " | Alternativ 2 = " + short_quiz_list_of_lists[0][2] + " | Alternativ 3 = " + short_quiz_list_of_lists[0][3])
anwser1 = get_int_input("Svara med siffrorna 1,2,3: ")
if anwser1 == 1:
    print("Rätt!")
else:
    print("Fel svar! svaret är " + short_quiz_list_of_lists[0][1])

#fråga 2

print(short_quiz_list_of_lists[1][0])
print("Alternativ 1 = " + short_quiz_list_of_lists[1][1] + " | Alternativ 2 = " + short_quiz_list_of_lists[1][2] + " | Alternativ 3 = " + short_quiz_list_of_lists[1][3])
anwser1 = get_int_input("Svara med siffrorna 1,2,3: ")
if anwser1 == 1:
    print("Rätt!")
else:
    print("Fel svar! svaret är " + short_quiz_list_of_lists[1][1])

print("---------Spelet är slut--------- \n")

#Uppgift 6 Inläsning av data till Quiz-spel med felhantering


def get_quiz_list_handle_exceptions():
    # sätter upp boolian för att senare ta mig vidare efter test
    file_format_and_exsist_test = False

    reset = input("Skriv in quiz filnamn:")  # här är filnamnet som ska testas
    while not file_format_and_exsist_test:
        in_file = reset
        # testar

        try:
            fr = open(in_file, "r")  # testar att öppna filen
            number_of_lines_counted = int(0)


        except FileNotFoundError:  # om filen inte existerar ger den en output
            print("Filen existerar inte!")
            reset = input("Skriv in ett nytt quiz filnamn: (glöm ej format) ")
            file_format_and_exsist_test = False

        else:
            for line in fr:  # testar så att varje rad följr formatet!
                file_count = line.count(";")
                count_of_semicolon = file_count
                if count_of_semicolon == 3:

                    print("raden ser bra ut")
                    file_format_and_exsist_test = True

                else:
                    file_format_and_exsist_test = False
                    fr.close()
                    reset = input("Filens format är fel! Du kan behöva kolla så att filen följer rätt protokoll! \n" "Skriv in en ny fil: ")
            fr.close()

    fr = open(reset, "r")

    list1 = []  # listan i list2
    list2 = []
    for line in fr:  # går igenom filen rad för rad

        de_junked = line.strip('\n')  # förstå hur strip funkar

        list1 = de_junked.split(';') # gör en lista vid ;
        print(list1)
        list2.append(list1)  # lägg till listan av fråga och svar i en position av listan som innehåller alla
    print(list2)
    fr.close()
                # print(text1)
                # text2 = text1.strip()
                # print(text2)
                # text3 = ['']
    returneringstext = "Din fil har hittats, kollats om den är i rätt format och gjorts till en lista redo att användas i ett quizz!"
    return returneringstext


print(get_quiz_list_handle_exceptions())


 # string.strip()
 # string.strip(";")


 #uppgift 7

 