def felhantering_heltal(utskriftstext):
    heltal = False
    while not heltal:
        try:
            anv_text = input(utskriftstext)
            anv_tal = int(anv_text)
        except ValueError:
            print('Ange ett heltal, försök igen')
        else:
            heltal = True
            return anv_tal

def felhantering_pin(utskriftstext):
    korrekt_format = False
    while not korrekt_format:
        anv_pin = felhantering_heltal(utskriftstext)
        if len(str(anv_pin)) == 4:
            korrekt_format = True
            return anv_pin
        else:
            print('Pin-koden måste vara 4 siffror, försök igen: ')

def visa_konton(konton):
    # Skriver ut alla namn och saldon från dictionaryn som en sträng med hjälp av __str__
    for key in konton:
        print(konton[key])

def meny():
    # Skriver ut menyn och anropar funktionen menyval
    print('-------------------------\n'
          '1 - Öppna nytt konto\n'
          '2 - Insättning\n'
          '3 - Uttag\n'
          '4 - Byta pin\n'
          '5 - Visa transaktioner\n'
          '6 - Avsluta\n'
          '-------------------------\n')
    anropa(menyval()) # Läser in menyvalet

def menyval():
    val = felhantering_heltal('Vad vill du göra? ')
    return val

def anropa(val):
    avsluta = False
    while not avsluta:
        if val != 1:
            try:
                namn = input('Ange kontots namn: ')
                account_dict[namn]
            except KeyError:
                print('Kontot finns inte, försök igen')
                meny()
        if val == 1:
            namn = input('Ange kontots namn: ')
            saldo = felhantering_heltal('Ange saldot: ')
            pin_kod = felhantering_pin('Ange en pin-kod: ')
            account_dict[namn] = Konto(namn, saldo, pin_kod) # Skapar ett nytt konto och lägger till i dictionaryn
            meny()

        elif val == 2:
            insattning = felhantering_heltal('Hur mycket vill du sätta in? ')
            account_dict[namn].insattning(insattning)
            meny()

        elif val == 3:
            if Konto.ok_pin(account_dict[namn]): # Kontrollerar pin-koden till kontot
                uttag = felhantering_heltal('Hur mycket vill du ta ut? ')
                account_dict[namn].uttag(uttag)
                meny()
            else:
                meny()

        elif val == 4:
            if Konto.ok_pin(account_dict[namn]): # Kontrollerar pin-koden till kontot
                account_dict[namn].byta_pin
                meny()
            else:
                meny()

        elif val == 5:
            print(account_dict[namn].transaktioner)
            meny()

        elif val == 6:
            avsluta = True


class Konto:
    def __init__(self, namn, saldo, pin_kod):
        self.namn = namn
        self.saldo = saldo
        self.pin_kod = pin_kod
        self.transaktioner = [] # Skapar en tom lista som transaktionerna läggs till i

    def __str__(self):
        return self.namn + '\n' + str(self.saldo) + 'kr' + '\n'

    def uttag(self, summa_uttag):
        # Tar bort en summa från saldot vid uttag av pengar
        if self.saldo > summa_uttag:
            self.saldo -= summa_uttag
            self.transaktioner.append(int('-' + str(summa_uttag))) # Lägger till uttaget i listan av transaktioner
            return self.saldo
        else:
            print('Transaktionen medges ej, du har för lite pengar på kontot')

    def insattning(self, summa_insattning):
        # Lägger till en summa till saldot vid insättning av pengar
        self.saldo += summa_insattning
        self.transaktioner.append(summa_insattning) # Lägger till insättningnen i listan av transaktioner
        return self.saldo

    def ok_pin(self):
        # Ber om koden och kollar så att den är rätt
        anv_pin = felhantering_pin('Ange pin-kod: ')
        if self.pin_kod == anv_pin:
            return True
        else:
            print('Fel pin-kod!')
            return False

    def byta_pin(self):
        # Ändrar pin-koden
        self.pin_kod = felhantering_pin('Ange en ny pin-kod: ')
        return self.pin_kod

class PremiumKonto(Konto):
    # Ärver alla Konto:s egenskaper men skriver över uttag
    def uttag(self, summa_uttag):
        if self.saldo > summa_uttag:
            Konto.uttag(self, summa_uttag) # Gör ett vanligt uttag om pengar finns på kontot
        else:
            input('Vill du ta ett lån? ')

account_dict = {}
account_dict["Lisa"] = Konto("Lisa", 200, 1111)
account_dict["Kalle"] = Konto("Kalle", 100, 2222)
account_dict["Kim"] = Konto("Kim", 300, 3333)
account_dict["Douglas"] = PremiumKonto("Douglas", 1000, 1234)


if __name__ == '__main__':
    meny()
    # visa_konton(account_dict)


