#Make sure to add term drescription and add automatic text
#Make sure to practice intermadiate list

#Multiline strings. 
#Before
#START: print("Summer will soon be over. Autumn is approaching. I want to see the snow in the mountains.")

#After. You can add space or other text inside.
#START: print("""Summer will soon be over. 
#Autumn is approaching. 
#END: I want to see the snow in the mountains.""")

#Concatenate with adding new line (\n). It's called new line indicator character.
#Before: print("What's your dog name?" + " My dog name is Batman.")
#After: print("What's your dog name? \n" + "My dog name is Batman.")

#Asterisk - To multiply: print("Marvel movies are awesome!" * 10)
#Use \n to make it cleaner: print("Marvel movies are awesome! \n" * 10)


#Network Chuck episode 2
#Building a video game

#Build a character

#print("Hello Adventurer! Welcome to Aurora's Adventures!!!")
#print("What is your name?")

#Input function
#START: input("What is your name?")

#START/END: print(input("What is your name?"))

#Create a Variable
#print("Hello ....... , we are happy to have you here!")

#Start:name = "Jasmine"
#print(name)
#name = "Ashton"
#END:print(name)

#Using the input() funtion with a variable 
#START: print("Hello Adventurer! Welcome to Aurora's Adventures!!!")

#name = input("What is your name?")

#END:print(name)

#Add with concatenate
#Start:print("Hello Adventurer! Welcome to Aurora's Adventures!!!")

#name = input("What is your name?\n")

#End: print("Hello " + name + ", we are happy to have you here!")

#Challenge 

#Start: print("Hello Adventurer! Welcome to Aurora's Adventures!!!")

#name = input("What is your name?\n")

#print("Hello " + name + ", we are happy to have you here!")

#characters = "Healer, Fighter, Archaeology, Pilot"

#print(name + ", choose your character! Each character have different abilities.\n" + characters)

#Selection = input()

#End: print("Wonderful choice " + name + "! You chose " + Selection + "! Your adventure starts now! We will meet again!")


#Network Chuck episode 3
#Math

#Integers
#Start: name = "Jasmine"
#age = 29

#print(name)
#End: print(age)

#Type() function
#Start:name = "Jasmine"

#age = 29

#age ="29"

#print(type(name))

#End:print(type(age))

#Floating point numbers/decimals
#Start: name = "Jasmine"

#age = 29

#actual_age = 29.96

#print(type(name))

#print(type(age))

#print(type(actual_age))

#Math calculator
#name = "Jasmine"

#age = 29

#actual_age = 29.96

#print(9+15)
#print(9-15)
#print(9/15)
#print(9*15)
#print(9*15/4**5)

#math = 9*15/4**5

#print(math)

#results = age + actual_age + math

#print (results) 



#(Modified) Building a video game/The int() function(converting data)
#Add Stop a number, add term descriptions,
#Start: 
#print("Hello Adventurer! Welcome to Aurora's Adventures!!!")

#name = input("What is your name?\n")

#print("Hello " + name + ", we are happy to have you here!")

#playergamemode = "easy mode, hard mode, extreme mode"

#gamemode = input("Choose a gamemode below you would like to play." "\n" + playergamemode + "\n")

#print("You've chosen " + gamemode + ".")

#characters = "Healer, Fighter, Archaeology, Pilot"

#ChooseCharacter = input(name + ", choose your character! Each character have different abilities. Check the options below." "\n" + characters + "\n")

#print("Awesome choice " + name + "!" " You will do well as a " + ChooseCharacter + "!")

#Upgrades1 = ("Speed boost, Wacky coins") 
#Boostprice = 2
#Coinsprice = 4

#buyupgrades = input("Would you like to buy upgrades? (Yes/No)\n")
#if buyupgrades == "Yes":
    #print("You chose to buy upgrades! You can buy up to 5 speed boost and 5 wacky coins each day.")
    #upgrades = input("Choose your upgrades below! \n" + Upgrades1 + "\n")
    #total = 0
    #if "Speed boost" in upgrades: 
       #quantity = input("How many speed boost do you want?\n")
       #total += Boostprice * int(quantity)
    #if "Wacky coins" in upgrades:
       #quantity2 = input("How many wacky coins do you want?\n")
       #total += Coinsprice * int(quantity2)
    #print("Your total is: $" + str(total))
#else:
    #print("You chose not to buy upgrades.")

#End
#print("Wonderful choice " + name + "! Your adventure starts now! We will meet again!")


#NetworkChuck Episode 4
#If (True) Else (False) statements. Nested ifs
#Need to add IF Else term descriptions
#start

#Using IF to control flow

#(Modified) Building a video game

#Start

#Add how to automatically talk

#print("Hello Adventurer! Welcome to Aurora's Adventures. Get Schwifty!!!")

#name = input("What is your name?\n")

#if name == "Rick":
    #print("Get out of here Rick!!! You're going to ruin my........")
    #exit()
#if name == "Rick Sanchez":
    #print("Get out of here Rick!!! You're going to ruin my........")
    #exit()
#if name == "Rick and Morty":
    #print("Get out of here Rick!!! You're going to ruin my........")
    #exit()
#else:
    #print("Hello " + name + ", we are happy to have you here!")

#playergamemode = "easy mode, hard mode, extreme mode"

#gamemode = input("Choose a gamemode below you would like to play." "\n" + playergamemode + "\n")

#print("You've chosen " + gamemode + ".")

#characters = "Healer, Fighter, Archaeology, Pilot"

#ChooseCharacter = input(name + ", choose your character! Each character have different abilities. Check the options below." "\n" + characters + "\n")

#print("Awesome choice " + name + "!" " You will do well as a " + ChooseCharacter + "!")

#Upgrades1 = ("Speed boost, Wacky coins") 
#Boostprice = 2
#Coinsprice = 4

#buyupgrades = input("Would you like to buy upgrades? (Yes/No)\n")
#if buyupgrades == "Yes":
    #print("You chose to buy upgrades! You can buy up to 5 speed boost and 5 wacky coins each day.")
    #upgrades = input("Choose your upgrades below! \n" + Upgrades1 + "\n")
    #total = 0
    #if "Speed boost" in upgrades: 
       #quantity = input("How many speed boost do you want?\n")
       #total += Boostprice * int(quantity)
    #if "Wacky coins" in upgrades:
       #quantity2 = input("How many wacky coins do you want?\n")
       #total += Coinsprice * int(quantity2)
    #print("Your total is: " + str(total))
#else:
    #print("You chose not to buy upgrades.")

#print("Wonderful choice " + name + "! Your adventure starts now! We will meet again!")

#End


#NetworkChuck Episode 5
#If Elif and Nested if

#Start

#print("Hello Adventurer! Welcome to Aurora's Adventures. Get Schwifty!!!")

#name = input("What is your name?\n")

#if name == "Rick":
    #suspiciousname = input("Are you Rick Sanchez?")
    #if suspiciousname == "Yes":
        #print("Get out of here Rick!!! You're going to ruin my........")
    #else:
        #print("Haha! You had me worried! You may enter!")
    #exit()
#if name == "Rick Sanchez":
    #print("Get out of here Rick!!! You're going to ruin my........")
    #exit()
#if name == "Rick and Morty":
    #print("Get out of here Rick!!! You're going to ruin my........")
    #exit()
#else:
    #print("Hello " + name + ", we are happy to have you here!")

#playergamemode = "easy mode, hard mode, extreme mode"

#gamemode = input("Choose a gamemode below you would like to play." "\n" + playergamemode + "\n")

#print("You've chosen " + gamemode + ".")

#characters = "Healer, Fighter, Archaeology, Pilot"

#ChooseCharacter = input(name + ", choose your character! Each character have different abilities. Check the options below." "\n" + characters + "\n")

#print("Awesome choice " + name + "!" " You will do well as a " + ChooseCharacter + "!")

#Upgrades1 = ("Speed boost, Wacky coins") 
#Boostprice = 2
#Coinsprice = 4

#buyupgrades = input("Would you like to buy upgrades? (Yes/No)\n")
#if buyupgrades == "Yes":
    #print("You chose to buy upgrades! You can buy up to 5 speed boost and 5 wacky coins each day.")
    #upgrades = input("Choose your upgrades below! \n" + Upgrades1 + "\n")
    #total = 0
    #if "Speed boost" in upgrades: 
       #quantity = input("How many speed boost do you want?\n")
       #total += Boostprice * int(quantity)
    #if "Wacky coins" in upgrades:
       #quantity2 = input("How many wacky coins do you want?\n")
       #total += Coinsprice * int(quantity2)
    #print("Your total is: " + str(total))
#else:
    #print("You chose not to buy upgrades.")

#Characterskins = ("Christmas, Halloween, Fruits, Aurora's Theme")

#Skins = input(name + " Would you like to get skins? See options below.\n" + Characterskins +"\n")

#if "Christmas" in Skins:
    #print("Price is $3!")
#elif "Halloween" in Skins:
    #print("Price is $4!")
#elif "Fruits" in Skins:
    #print("Price is free!")
#elif "Aurora's Theme" in Skins:
    #print("Price is free!")
#else:
    #print("We do not have that skin, maybe in the future we will.")

#Options = "Tutorial, No tutorial"

#Chooseoption = input("Would you like to do the tutorial?\n" + Options + "\n")

#if Chooseoption == "Tutorial":
    #print("Wonderful choice " + name + "! Let's enter the training room!")
#elif Chooseoption == "No tutorial":
    #print("Wonderful choice " + name + "! Your adventure starts now! We will meet again!")

#End



#Networkchuck Episode 6
#logical Operators

#Start

#print("Hello Adventurer! Welcome to Aurora's Adventures. Get Schwifty!!!")

#name = input("What is your name?\n")

#if name == "Rick" or name == "Morty":
    #suspiciousname = input("Are you Rick Sanchez?")
    #crimes = int(input("How many crimes have you committed?"))
    #if suspiciousname == "Yes" and crimes <= 8000000:
        #print("Get out of here " + name + "!!! You're going to ruin my........")
        #exit()
    #else:
        #print("Haha! You had me worried! You may enter!")
#if name == "Rick Sanchez" or name == "Morty Smith":
    #print("Get out of here Rick!!! You're going to ruin my........")
    #exit()
#if name == "Rick and Morty":
    #print("Get out of here Rick!!! You're going to ruin my........")
    #exit()
#else:
    #print("Hello " + name + ", we are happy to have you here!")

#playergamemode = "easy mode, hard mode, extreme mode"

##gamemode = input("Choose a gamemode below you would like to play." "\n" + playergamemode + "\n")

#print("You've chosen " + gamemode + ".")

#characters = "Healer, Fighter, Archaeology, Pilot"

#ChooseCharacter = input(name + ", choose your character! Each character have different abilities. Check the options below." "\n" + characters + "\n")

#LionRoar8KMFact = "True"
#LionRoarFact = "False, a lion's roar can be heard up to eight kilometres away "

#if ChooseCharacter == "Archeaology":
    #fact = input("A lion's roar can be heard up to eight kilometres away (Yes/No)\n")
    #if fact == "Yes":
        #print(LionRoar8KMFact)
    #if fact == "No":
        #print(LionRoarFact)
#if not name == "Healer, Fighter, Pilot":
    #print("Awesome choice " + name + "!" " You will do well as a " + ChooseCharacter + "!")

#The common way to use 'Not' is to use '!='
#Example 
# if name != "Healer, Fighter, Pilot":
    #print("Awesome choice " + name + "!" " You will do well as a " + ChooseCharacter + "!")

#Boolean True or False, YT NetworkChuck 15:56
#LionRoar8KMFact == "True"
#not LionRoar8KMFact == "True"
#LionRoar8KMFact == "Tough"
#print(type(LionRoar8KMFact == "True"))

#Upgrades1 = ("Speed boost, Wacky coins") 
#Boostprice = 2
#Coinsprice = 4

#buyupgrades = input("Would you like to buy upgrades? (Yes/No)\n")
#if buyupgrades == "Yes":
    #print("You chose to buy upgrades! You can buy up to 5 speed boost and 5 wacky coins each day.")
    #upgrades = input("Choose your upgrades below! \n" + Upgrades1 + "\n")
    #total = 0
    #if "Speed boost" in upgrades: 
       #quantity = input("How many speed boost do you want?\n")
       #total += Boostprice * int(quantity)
    #if "Wacky coins" in upgrades:
       #quantity2 = input("How many wacky coins do you want?\n")
       #total += Coinsprice * int(quantity2)
    #print("Your total is: " + str(total))
#else:
    #print("You chose not to buy upgrades.")

#Characterskins = ("Christmas, Halloween, Fruits, Aurora's Theme")

#Skins = input(name + " Would you like to get skins? See options below.\n" + Characterskins +"\n")

#if "Christmas" in Skins:
    #print("Price is $3!")
#elif "Halloween" in Skins:
    #print("Price is $4!")
#elif "Fruits" in Skins:
    #print("Price is free!")
#elif "Aurora's Theme" in Skins:
    #print("Price is free!")
#else:
    #print("We do not have that skin, maybe in the future we will.")

#Options = "Tutorial, No tutorial"

#Chooseoption = input("Would you like to do the tutorial?\n" + Options + "\n")

#if Chooseoption == "Tutorial":
    #print("Wonderful choice " + name + "! Let's enter the training room!")
#elif Chooseoption == "No tutorial":
    #print("Wonderful choice " + name + "! Your adventure starts now! We will meet again!")

#End


#Networkchuck Episode 7
#list in Python

#Start

print("Hello Adventurer! Welcome to Aurora's Adventures. Get Schwifty!!!")

name = input("What is your name?\n")

if name == "Rick" or name == "Morty":
    suspiciousname = input("Are you Rick Sanchez?")
    crimes = int(input("How many crimes have you committed?"))
    if suspiciousname == "Yes" and crimes <= 8000000:
        print("Get out of here " + name + "!!! You're going to ruin my........")
        exit()
    else:
        print("Haha! You had me worried! You may enter!")
if name == "Rick Sanchez" or name == "Morty Smith":
    print("Get out of here Rick!!! You're going to ruin my........")
    exit()
if name == "Rick and Morty":
    print("Get out of here Rick!!! You're going to ruin my........")
    exit()
else:
    print("Hello " + name + ", we are happy to have you here!")

playergamemode = "easy mode, hard mode, extreme mode"

gamemode = input("Choose a gamemode below you would like to play." "\n" + playergamemode + "\n")

print("You've chosen " + gamemode + ".")

characters = "Healer, Fighter, Archaeology, Pilot"

ChooseCharacter = input(name + ", choose your character! Each character have different abilities. Check the options below." "\n" + characters + "\n")

LionRoar8KMFact = "True"
LionRoarFact = "False, a lion's roar can be heard up to eight kilometres away "

if ChooseCharacter == "Archeaology":
    fact = input("A lion's roar can be heard up to eight kilometres away (Yes/No)\n")
    if fact == "Yes":
        print(LionRoar8KMFact)
    if fact == "No":
        print(LionRoarFact)
if not name == "Healer, Fighter, Pilot":
    print("Awesome choice " + name + "!" " You will do well as a " + ChooseCharacter + "!")

#The common way to use 'Not' is to use '!='
#Example 
# if name != "Healer, Fighter, Pilot":
    #print("Awesome choice " + name + "!" " You will do well as a " + ChooseCharacter + "!")

#Boolean True or False, YT NetworkChuck 15:56
#LionRoar8KMFact == "True"
#not LionRoar8KMFact == "True"
#LionRoar8KMFact == "Tough"
#print(type(LionRoar8KMFact == "True"))

Upgrades1 = ("Speed boost, Wacky coins") 
Boostprice = 2
Coinsprice = 4

buyupgrades = input("Would you like to buy upgrades? (Yes/No)\n")
if buyupgrades == "Yes":
    print("You chose to buy upgrades! You can buy up to 5 speed boost and 5 wacky coins each day.")
    upgrades = input("Choose your upgrades below! \n" + Upgrades1 + "\n")
    total = 0
    if "Speed boost" in upgrades: 
       quantity = input("How many speed boost do you want?\n")
       total += Boostprice * int(quantity)
    if "Wacky coins" in upgrades:
       quantity2 = input("How many wacky coins do you want?\n")
       total += Coinsprice * int(quantity2)
    print("Your total is: " + str(total))
else:
    print("You chose not to buy upgrades.")

Characterskins = ("Christmas, Halloween, Fruits, Aurora's Theme")

Skins = input(name + " Would you like to get skins? See options below.\n" + Characterskins +"\n")

if "Christmas" in Skins:
    print("Price is $3!")
elif "Halloween" in Skins:
    print("Price is $4!")
elif "Fruits" in Skins:
    print("Price is free!")
elif "Aurora's Theme" in Skins:
    print("Price is free!")
else:
    print("We do not have that skin, maybe in the future we will.")

Adventure_area = ["Haunted Cemetery", "Breathing Forest", "Old woman House", "Haunted Hotel"]
#Adventure area, Health, Only heartbeat it should be in bpm, Is it scary?) 
Adventure_area1 = ["Haunted Cemetery", 200, 105.000, False]
Adventure_area2 = ["Breathing Forest", 200, 105.000, False]
Adventure_area3 = ["Old Woman House", 150, 90.000, True]
Adventure_area4 = ["Haunted Hotel", 100, 90.000, True]

area = input(f"Choose an area you want to do below. You'll be able to see required task and information about the area you selected. Information: Adventure area, starting health amount, game over if you pass this heartbeat, and is it scaary?\n {Adventure_area}""\n")

if "Haunted Cemetery" in area: 
    print(Adventure_area1)
elif "Breathing Forest" in area:
    print(Adventure_area2)
elif "Old Woman House" in area:
    print(Adventure_area3)
elif "Haunted Hotel" in area:
    print(Adventure_area4)

Adventure_list = ["Flash light", "Map", "Backpack", "Binoculars"]

print("These are the items you are provided with!" "\n" , Adventure_list ,)

#print(type(Adventure_list))

Extra_items = ("Nunchucks, Medkits, Dental picks, Tool kit")

items = input("Would you like to add extra items below? (Yes/No) \n")

if items == "Yes":
    Select_items = input("Select the items you want: " , Extra_items , "\n") 
    print(Select_items + " Will be added to your inventory.")
if items == "No":
    print("You decided not to add extra items!")

Options = "Tutorial, No tutorial"

Chooseoption = input("Would you like to do the tutorial?\n" + Options + "\n")

if Chooseoption == "Tutorial":
    print("Wonderful choice " + name + "! Let's enter the training room!")
elif Chooseoption == "No tutorial":
    print("Wonderful choice " + name + "! Your adventure starts now! We will meet again!")



#End
