
import copy
import math
import random

# Uppgift 1 (givet)

def scope_testing_function(x, x_list):
    print("Inside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
    x = 1
    x_list[0] = 1
    print("Inside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
    x_list = [1, 2, 3, 4]
    print("Inside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
    return x

x_list = [11, 22, 33, 44]
x = 11
y = 22
print("Outside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))

scope_testing_function(x, x_list)
print("Outside function: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))

# Uppgift 2 (att skrivas)
def my_function(x): #annat x
    y = (math.sin(x))**2 + x**2
    return y

# Uppgift 3 (att skrivas)
def roll_dice(n):
    result = 0
    for i in range (0,n):
        result += random.randint(1,6)
    return result


# Uppgift 4 (att skrivas)
def my_sort_list(list1):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, len(list1)-1):
            if list1[i] > list1[i+1]:
                sorted = False
                temp = list1[i]
                list1[i] = list1[i+1]
                list1[i+1] = temp
                #alternativ i python list1[i], list[i+1] = list[i+1], list[i]
    return list1


# Uppgift 5 (att skrivas)
def bandit_language(string):
    lower_string = str.lower(string) #konvertera till små bokstäver
    chars = [] #
    for line in lower_string:
        chars.extend(line) #lägger till en karaktär i listan för varje gång den körs
    amount_of_chars = len(chars) #räknar längeden av listan
    for i in range (0, amount_of_chars):
        kons = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z"]
        length_kons = len(kons)
        for k in range (0,length_kons):
            if chars[i] == kons[k]: #om det är en konsonant
                chars [i] += ("o" + chars[i]) # lägg till o och själva konsonanten efter
    lower_string_bandit = "".join(chars) #konvertera till en sträng igen, varför fnuttar?
    return lower_string_bandit



