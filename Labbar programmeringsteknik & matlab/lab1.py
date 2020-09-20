#Uppgift 1.1
nice_name = 'Kim'
print (nice_name)

#uppgift 1.2
long_name = ""
for i in range (0, 33): #long_name är som en counter i loopen
    long_name += nice_name
print (long_name)

#Uppgift 2
user_name1 = input("Vad heter du? ")

for y in range(0, 39):
    print (user_name1)

#Uppgift 3
user_name2 = "" #ge den start"värde"
while (user_name2 != "Sauron" and user_name2 != "sauron"): #and eftersom båda måste gälla samtidigt i loopen
    user_name2 = input("Vad heter du? ")
    print("hej " + user_name2)
print ("Välkommen härskare Sauron")

#Uppgift 4
# print(1 == 0.99)
# false
# print(1 == 0.99999999999)
# false
# print(1 == 0.99999999999999999999)
# true
#
# Detta beror på avrundningen som sker när en float används som har fler än 16 decimaler.

#Uppgift 5
import math
sum = 0
n = int(input("n = ")) #begär slutpunkt
for k in range(1, n+1):
    equation = 1/(k**2)
    sum += equation

infinate = math.pi**2/6
print(sum)
print(infinate - sum)


