# Writer:
# Date: 12 november 2014 

# Animal ckass that defines what is relevant of the animals in the given problem, 
# used for object creation of each animal found in animal.txt
class Animal(object):
	
	def __init__(self, name, seasonSleep, wakeTime, sleepTime, feedTime):
		self.name = name
		self.seasonSleep = seasonSleep
		self.wakeTime = int(wakeTime)
		self.sleepTime = int(sleepTime)
		self.feedTime = int(feedTime)
		
# Reads animal.txt creating objects for each row, stores in a list and returns the list
def file_reader():
	animalList = []
	file_object = open("animal.txt", "r", encoding="utf-8") # encoding utf-8 for reading "ÅÄÖ"
	file_object.readline() # reads first line "Format: ...", does not store it
	
	# Walks through the textfile, creating an object for each that are stored in animalList
	for i in range(0,7):
		string_list = file_object.readline().replace("\n","").split("/") # removes all 'enter' and splits into a list, divided by "/""
		awakeTime = string_list[2].split("-") # Further splits the awaketime of the animals into waketime and sleeptime as a list
		animalList.append(Animal(string_list[0], string_list[1], awakeTime[0], awakeTime[1], string_list[3])) # Creates an object of the extracted data from the current row using Animal-class
	return animalList

# filters the available animals by the current season, adds them to a separate list filtered_animal_list
def season_filter(animal_list, current_season):
	
	filtered_animal_list = []
	for animal in animal_list: # for each animal-object in the list, do:
		if animal.seasonSleep == current_season: # if it is the nap-season for the animal
			pass # do nothing
		else:	# if th is NOT the nap-season, (the animal is available)
			filtered_animal_list.append(animal)			# add the animal to the filtered list
	return filtered_animal_list

# gets the input required for the program to run, returns all the inputted data
def inital_input():
	while True: # while-true loop, will keep looping until all inputs are acceptable 
		date = input("Var god välj DATUM för besöket (1-31): ")
		month = input("Var god välj MÅNAD för besöket (1-12): ")
		timeArrival = input("Var god välj ANKOMSTTID för besöket, svara avrundat till timmar (0-24): ")
		timeHome = input("Var god välj AVFÄRDSTID för besöket, svara avrundat till timmar (0-24): ")

		if date.isdigit() and month.isdigit() and timeArrival.isdigit() and timeHome.isdigit(): # if the user has inputed digits do:

			# if all inputs are acceptable, do:
			time_open = 8
			time_close = 24
			if int(timeArrival) < int(timeHome) and int(timeArrival) >= time_open and int(timeArrival) <= time_close and int(timeHome) >= 1 and int(timeHome) <= 20 and int(date) >= 1 and int(date) <= 31 and int(month) >= 1 and int(month) <= 12:
				if (int(date) <= 28 and int(month) == 2) or int(month) != 2:
					break # break the while-loop
				else:
					print("Februari har 28 dagar!")
			# if the inputs are digits but still not acceptable, do:
			else:
				# Some unaccepted input
				if int(timeArrival) >= int(timeHome):
					print("Ankommstid måste vara före AVFÄRDSTID!")
				# elif (int(date) > 28 and int(month) == 2):
				# 	print("Februari har 28 dagar!")
				elif int(timeArrival) < 8:
					print("Parken öppnar vid 8, var god revidera ANKOMSTTID")
				elif int(timeHome) > 18:
					print("Parken stänger vid 18, var god revidera AVFÄRDSTID")
				else:
					print("Var god och följ instruktionerna!")

		# if the input was not in digits
		else:
			print("Inmatning måste vara enbart med siffror!!")

	return date, month, timeArrival, timeHome

# gets the season depending on which month it is, returns the season-name
def season_get(month):
	if month == 12 or month == 1 or month == 2:	# Winter
		return "vinter"
	elif month == 3 or month == 4 or month == 5: # Spring
		return "vår"
	elif month == 6 or month == 7 or month == 8: # Summer
		return "sommar"
	elif month == 9 or month == 10 or month == 11: # Autumn
		return "höst"

# further filters the animals by time and feedtime, generates a string that is printed
def available_animals(animal_list, arrival, home):
	to_be_printed = "\n\nVakna djur under besöket:\n\n"

	# walk through the season-filtered animallist
	for animal in animal_list:


		# Now filter by time as well, covering all four cases that could occur, the animals that are asleep will not be included
		if (animal.wakeTime >= arrival and animal.sleepTime <= home and animal.sleepTime > animal.wakeTime) or (animal.wakeTime >= arrival and animal.sleepTime >= home) or (animal.wakeTime <= arrival and animal.sleepTime <= home) or (animal.wakeTime <= arrival and animal.sleepTime >= home):

			# also filter by feedtime, presenting the time that the animals are fed if it is whithin the visiting hours
			if ((animal.feedTime >= arrival and animal.feedTime <= home) or (animal.feedTime <= arrival and animal.feedTime >= home)):
				to_be_printed = to_be_printed + animal.name + "         *** matas kl " + str(animal.feedTime) + " ***\n"
			
			# if the animals is not fed during the visit-hours, just add the animal's name
			else:
				to_be_printed = to_be_printed + animal.name + "\n"
	print(to_be_printed) # finally print the string of all available animals, and if they are fed, what time.


print("INSTRUKTIONER: All inmatning MÅSTE ske med siffror!!")
animals = file_reader() # Reads the animal.txt, returns the list containing the animals
date, month, timeArrival, timeHome = inital_input() # gets the input required to run the program
season = season_get(int(month)) # gets which season that corresponds to which month
filtered_animals = season_filter(animals, season) # filters animals by season
available_animals(filtered_animals, int(timeArrival), int(timeHome)) # filters animals my awaketime and feedtime, prints result
print("\nTrevligt återbesök!")

		





