
def create_file_from_string(filename, my_string):
#Skapar en fil med namnet filename (en sträng) och fyller den med innehållet i my_string (en sträng)
    fw = open(filename, 'w') #skapar en ny fil som ska gå att skriva i fw = filewrite
    fw.write(my_string + '\n') #skriver en sträng i filen sedan nyrad
    fw.close() #stänger filen

def print_file_on_screen(filename):
#Öppnar filen med namnet filename (en sträng) och skriver ut innehållet på skärmen
    fr = open(filename, 'r') #fw = fileread, öppnar och läser en fil
    text = fr.read() #stoppar in den lästa strängen i en variabel
    print(text) #skriver ut innehållet i variabeln text som är innehållet i filen
    fr.close()
'''
test
create_file_from_string('min_superfil.txt', 'hurra för mig')
print_file_on_screen('min_superfil.txt')
'''
string = "katt"
print(int(string))