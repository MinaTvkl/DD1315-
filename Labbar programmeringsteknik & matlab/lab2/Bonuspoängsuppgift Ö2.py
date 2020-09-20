#Uppgift 1
def rectangle_area(height, width):
    area = height*width #beräknar arean med hjälp av höjd och bredd
    return area #returnera arean

#Uppgift 2
def rectangle_circumference(height, width):
    circumference = 2*(height+width) #beräknar omkretsen med hjälp av höjd och bredd
    return circumference #returnera omkretsen


#test! kallar på funktionerna ovan
#user_height = int(input("Rectangle height: "))
#user_width = int(input("Rectangle width: "))

#print(rectangle_area(user_height, user_width))
#print(rectangle_circumference(user_height, user_width))

#Uppgift 3
def third_charachter_of_string(string):
    if len(string) < 3: #om längden av strängen är mindre än 3 tecken returneras False då den är för kort
        return False
    else:
        third_character = string[2] #annars plockas det tredje tecknet ut (börjar från 0) och returneras
        return third_character

#test! kallar på funktionen ovan
print(third_charachter_of_string(input("Skriv något: ")))

