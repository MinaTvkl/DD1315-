def get_quiz_list_handle_exceptions():
    file_exists = False
    while not file_exists:  # loopar ifall in filen inte finns
        try:
            in_file = input("Filnamn: ")
            fr = open(in_file, 'r')  # testar att öppna och läsa filen
        except FileNotFoundError:
            print("Filen hittas inte, försök igen: ")

        else:
            file_exists = True  # hoppar ur loopen om filen finns
            list1 = []
            list2 = []
            i = 0
            for line in fr: #går igenom filen rad för rad
                print(line)
                de_junked = line.strip('\n') #förstå hur strip funkar
                print(de_junked)
                list1 = line.split(';') #gör en lista vid ;
                list2.append(list1) #lägg till listan av fråga och svar i en position av listan som innehåller allt
            print(list2)
            cat = "ttkattentt"
            cat2 = cat.strip('t')
            print(cat.strip('t'))
            str = "0000000this is string example....wow!!!0000000";
            print(str.strip('0'))

            fr.close()
           # print(text1)
            #text2 = text1.strip()
            #print(text2)
            #text3 = ['']

get_quiz_list_handle_exceptions()