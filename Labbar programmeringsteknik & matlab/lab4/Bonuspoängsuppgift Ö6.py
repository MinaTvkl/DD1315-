class Student:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    def print_firstname(self):
        print(self.firstname)

kim = Student('Kim', 'Johansson')
kim.print_firstname()

class Medieteknikstudent(Student): #använder student som förälder och tar efter dess egenskaper

    def print_greeting(self): #lägger till en funktion utöver students funktioner
        print('Welcome to school!')

kim = Medieteknikstudent('Kim', 'Johansson')
kim.print_firstname()
kim.print_greeting()

