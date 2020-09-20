
#Input funktioner
#______________________________________________

def get_int_input(prompt_string):
    integer = False
    while not integer:
        try:
            user_in = input(prompt_string) #ifall det inte är  en int
            int_user_in = int(user_in)
        except:
            print("Ange ditt val med en siffra") #så börjar vi om efter som integer inte är True

        else:
            integer = True #Så kommer den avsluta
    return int_user_in


def get_user_text_input(prompt_string):
    true = False
    while not true:
        try:
            namn = input(prompt_string)
            test_name = int(namn)
        except ValueError:
            true = True
        else:
            print("Det får inte vara en siffra")
    return namn

def get_four_dig_input(prompt_string):
    true = False
    while not true:
        pin_kod = get_int_input(prompt_string)
        if len(str(pin_kod)) == 4:
            true = True
        else:
            print("Din kod måste vara 4 siffror")

    return pin_kod

#__________________________________________________
#Klasser
class konto:

    def __init__(self, namn, pengar, pin_kod):    #börjar en klass med init och skriver in variabler i den ordning de skall vara i listan på personen
        self.namn = namn
        self.pengar = pengar
        self.pin_kod = pin_kod
        self.transaktioner = []



    def __str__(self):
        return self.namn + "\n"+ str(self.pengar) + "kr" #printar namnet man skriver in och hur mycket pengar den har på kontot


    def uttag(self, ut):

        if self.pengar > ut:  #kollar om det finns pengar på kontot
            self.pengar -= ut #tar ut pengar från kontot
            self.transaktioner.append(int("-" + str(ut))) #lägger till det nya saldot i transaktionslistan
            return self.pengar
        else:
            print("Transaktion medges ej")

        return self.pengar

    def insattning(self, insättning):

        self.pengar += insättning  #lägger till insättningen till saldot
        self.transaktioner.append(insättning) #lägger till nytt saldo i listan
        return self.pengar

    def ok_PIN(self):
        pin = get_four_dig_input("Pinkod:") #låter användaren skriva in pinkod
        if pin == self.pin_kod: #kollar om pinkoden stämmer överens med den i listan
            return True
        else:
            return False


    def byta_PIN(self):
        byta_kod = get_four_dig_input("byta kod:") #låter anvädaren skriva in ny pinkod
        self.pin_kod = byta_kod #ersätter gamla koden med nya
        return "ny kod:" + str(self.pin_kod) #skiver ut den nya koden på skärmen

class PremiumKonto(konto):  #ärver allt från konto och lägger till funktion om lånerbjudande
    def uttag(self, belopp): #ersätter det gamla uttag, belopp ersätter ("uttag:") i val==3

        if self.pengar > belopp: #om det finns pengar på kontot kör den vanliga uttag
            konto.uttag(self, belopp)
        else:
            print("vill du ta ett lån?")


account_dict = {}
account_dict["Lisa"] = konto("Lisa", 345, 1234)
account_dict["Kalle"] = konto("Kalle", 222, 1234)
account_dict["Kim"] = konto("Kim", 123, 1234)
account_dict["Douglas"] = PremiumKonto("Douglas", 5, 1234)


#funktioner
#______________________________________________

def visa_konto(konto):
    for value in konto:
        print(konto[value]) #printar användarens namn och saldo (på grund av __str__(self) högre upp

def meny():
    print("Välkommen till Simon Banken! \n______________________________________________\nMeny:\n1 - Öppna nytt konto\n2 - Insättning\n3 - Uttag\n4 - Byta pin\n5 - Visa transaktioner\n6 - Avsluta\n----------------------------------------------")
    menyval() #startar nästa

def menyval():
    val = get_int_input("Val:") #använder get int input för att hämta valet
    anropa(val)  #startar nästa funktion beroende på vad användaren valt

def anropa(val):

    if val != 6:
        namn = get_user_text_input("kontots namn:")

        if val == 1:

            belopp = get_int_input("belopp:")
            pin = get_four_dig_input("pin:")
            account_dict[namn] = konto(namn, belopp, pin) #skapas en ny användare i dictionaryn med de valda koderna osv
            meny() #börjar om

        elif val == 2:
            account_dict[namn].insattning(get_int_input("insättning:"))
            #går upp till tidigare def om insättning för det namn man har skrivit i
            meny()

        elif val == 3:
            if konto.ok_PIN(account_dict[namn]) == True: #kontrollerar om pinkoden stämmer
                account_dict[namn].uttag(get_int_input("uttag:")) #kontrollera om namnet tillhör konto eller premiumkonto, väljer därefter vilket uttag som är aktuellt
                meny()
            else:
                print("fel kod")
                meny()

        elif val == 4:
            if konto.ok_PIN(account_dict[namn]) == True:
                konto.byta_PIN(account_dict[namn])
                meny()
            else:
                print("fel kod")
                meny()

        elif val == 5:
            if konto.ok_PIN(account_dict[namn]) == True:
                print(account_dict[namn],"\n" "Transaktioner:", account_dict[namn].transaktioner)
                meny()
    else:
        print("hejdå")

meny()