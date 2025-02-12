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



#(Modified) Building a video game

#Start: Fix the variable not connect
print("Hello Adventurer! Welcome to Aurora's Adventures!!!")

name = input("What is your name?\n")

print("Hello " + name + ", we are happy to have you here!")

playergamemode = "easy mode, hard mode, extreme mode"

gamemode = input("Choose a gamemode below you would like to play." "\n" + playergamemode + "\n")

print("You've chosen " + gamemode + ".")

characters = "Healer, Fighter, Archaeology, Pilot"

ChooseCharacter = input(name + ", choose your character! Each character have different abilities. Check the options below." "\n" + characters + "\n")

print("Awesome choice " + name + "!" " You will do well as a " + ChooseCharacter + "!")

buyupgrades = input("Would you like to buy upgrades? (Yes/No)\n")
if buyupgrades == "Yes":
    print("You chose to buy upgrades!")
else:
    print("You chose not to buy upgrades.")

upgrades = ("Speed boost, Wacky coins")

print("Choose an upgrade below.\n" + upgrades)

boost = "$2"
coins = "$4" 
quantity = input()


#End: 
#print("Wonderful choice " + name + "! You chose " + Selection + "! Your adventure starts now! We will meet again!")
