
import my_module



# Uppgift 1 (givet)

y = 222
x = 111
x_list = [111, 222, 333, 444]
print("Outside module: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
my_module.scope_testing_function(x, x_list)
print("Outside module: x=" + str(x) + " and x_list=" + str(x_list) + " and y=" + str(y))
#de har kopplat ihop filen my_module med denna så att funktionen kan kallas på i denna fil

# Uppgift 2 (att skrivas)
x1 = 2
x2 = 5
x3 = 3
print(my_module.my_function(x1))
print(my_module.my_function(x2))
print(my_module.my_function(x3))

# Uppgift 3 (att skrivas)
number_of_dices = int(input("Skriv antalet tärningar: "))
print(my_module.roll_dice(number_of_dices)) #kallar på funktionen

# Uppgift 4 (att skrivas)
unsorted_list = [1, 10, 300, 20, 50, 7, 1, 2]
print(unsorted_list)
sorted_list = (my_module.my_sort_list(unsorted_list))
print(sorted_list)

# Uppgift 5 (att skrivas)
to_become_bandit = input("Skriv din text som ska göras om till rövarspråk!")
print(my_module.bandit_language(to_become_bandit))

# Uppgift 6 (givet)
animals = {'tiger': ['claws', 'sharp teeth', 'four legs', 'stripes'],
           'elephant': ['trunk', 'four legs', 'big ears', 'gray skin'],
           'human': ['two legs', 'funny looking ears', 'a sense of humor']
           }

# Uppgift 6 (att skrivas)
def make_bandit_dictionary(dict):

    for key in dict: #går igenom dictionary med hjälp av en tom variabel som ersätts med en key i taget
        dict[key] = [my_module.bandit_language(i) for i in dict[key]] #i är position i listan för en specifik key
    #denna position ersätts med motsvarande sträng i rövarspråk
    dict
    return dict

#rovar_animals = make_bandit_dictionary(animals)
#print(rovar_animals)



