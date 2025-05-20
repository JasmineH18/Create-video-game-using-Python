# Resoucres Used:
- https://www.python.org/doc/

# Environments Used:
- Visual Studio Code on Windows and MacOS 

# Video Game Scenario

Multiline strings. 
```
print("Summer will soon be over. Autumn is approaching. I want to see the snow in the mountains.")
```
Output: 
<br>
Summer will soon be over. Autumn is approaching. I want to see the snow in the mountains.
<br><br>

You can add space or other text inside using three quotation marks.
```
print("""Summer will soon be over. 
Autumn is approaching. 
I want to see the snow in the mountains.""")
```
Output:
<br>
Summer will soon be over. 
<br>
Autumn is approaching.
<br>
I want to see the snow in the mountains.
<br><br><br>

Concatenate with adding new line '\n'. It's called new line indicator character.
```
print("What's your dog name? \n" + "My dog name is Batman.")
```
Output: 
<br>
What's your dog name? 
<br>
My dog name is Batman.
<br><br><br>

Asterisk - To multiply:
```
print("Marvel movies are awesome!" * 10)
```
Output:
<br>
Marvel movies are awesome!Marvel movies are awesome!Marvel movies are awesome!
<br>
Marvel movies are awesome!Marvel movies are awesome!Marvel movies are awesome!
<br>
Marvel movies are awesome!Marvel movies are awesome!Marvel movies are awesome!
<br>
Marvel movies are awesome!
<br><br>

#Use \n to make it cleaner
```
print("Marvel movies are awesome! \n" * 10)
```
Output:
<br>
Marvel movies are awesome! 
<br>
Marvel movies are awesome! 
<br>
Marvel movies are awesome! 
<br>
Marvel movies are awesome! 
<br>
Marvel movies are awesome! 
<br>
Marvel movies are awesome! 
<br>
Marvel movies are awesome! 
<br>
Marvel movies are awesome! 
<br>
Marvel movies are awesome! 
<br>
Marvel movies are awesome!
<br><br><br>

# Building a video game
# Part 1

Building a character
```
print("Hello Adventurer! Welcome to Aurora's Adventures!!!")
print("What is your name?")
```
Output:
<br>
Hello Adventurer! Welcome to Aurora's Adventures!!!
<br>
What is your name?
<br><br>

Input function: The code gather the user's answer.
```
input("What is your name?")
```
Output:
<br>
What is your name?Jasmine
<br>
Blank output
<br><br>

Correct way.
```
print(input("What is your name?"))
```
Output:
<br>
What is your name? Jasmine
<br>
 Jasmine
<br><br>

Create a Variable.
<br>
```
name = "Jasmine"
print(name)

name = "Ashton"
print(name)
```
Output:
<br>
Jasmine
<br>
Ashton
<br><br>

Using the input() funtion with a variable 
```
print("Hello Adventurer! Welcome to Aurora's Adventures!!!")

name = input("What is your name?\n")

print(name)
```
Output:
<br>
Hello Adventurer! Welcome to Aurora's Adventures!!!
<br>
What is your name?
<br>
Jasmine
<br>
Jasmine
<br><br>

Add with concatenate
```
print("Hello Adventurer! Welcome to Aurora's Adventures!!!")

name = input("What is your name?\n")

print("Hello " + name + ", we are happy to have you here!")
```
Output:
<br>
Hello Adventurer! Welcome to Aurora's Adventures!!!
<br>
What is your name?
<br>
Jasmine
<br>
Hello Jasmine, we are happy to have you here!
<br><br>

Add more to the code. 
```
print("Hello Adventurer! Welcome to Aurora's Adventures!!!")

name = input("What is your name?\n")

print("Hello " + name + ", we are happy to have you here!")

characters = "Healer, Fighter, Archaeology, Pilot"

print(name + ", choose your character! Each character have different abilities.\n" + characters)

Selection = input()

print("Wonderful choice " + name + "! You chose " + Selection + "! Your adventure starts now! We will meet again!")
```
Output:
<br>
Hello Adventurer! Welcome to Aurora's Adventures!!!
<br>
What is your name?
<br>
Jasmine
<br>
Hello Jasmine, we are happy to have you here!
<br>
Jasmine, choose your character! Each character have different abilities. <br>
Healer, Fighter, Archaeology, Pilot <br>
Pilot <br>
Wonderful choice Jasmine! You chose Pilot! Your adventure starts now! We will meet again! <br><br>


# Part 2: Math

Integers 
```
name = "Jasmine" 
age = 29

print(name)
print(age)
```
Output: <br>
Jasmine <br>
29 <br><br>

Type() function 
```
name = "Jasmine"

age = 29

print(type(name))

print(type(age))
```
Output: <br>
<class 'str'> <br>
<class 'int'> <br><br>

Floating point numbers/decimals
```
name = "Jasmine"

age = 29

actual_age = 29.96

print(type(name))

print(type(age))

print(type(actual_age))
```
Output: <br>
<class 'str'> <br>
<class 'int'> <br>
<class 'float'> <br><br>

Math calculator
```
name = "Jasmine"

age = 29

actual_age = 29.96

print(9+15)
print(9-15)
print(9/15)
print(9*15)
print(9*15/4**5)

math = 9*15/4**5

print(math)

results = age + actual_age + math

print (results)
```
Output: <br>
24 <br>
-6 <br>
0.6 <br>
135 <br>
0.1318359375 <br>
0.1318359375 <br>
59.0918359375 <br><br>

(Modified) Building a video game. The int() function(converting data)
```
print("Hello Adventurer! Welcome to Aurora's Adventures!!!")

name = input("What is your name?\n")

print("Hello " + name + ", we are happy to have you here!")

playergamemode = "easy mode, hard mode, extreme mode"

gamemode = input("Choose a gamemode below you would like to play." "\n" + playergamemode + "\n")

print("You've chosen " + gamemode + ".")

characters = "Healer, Fighter, Archaeology, Pilot"

ChooseCharacter = input(name + ", choose your character! Each character have different abilities. Check the options below." "\n" + characters + "\n")

print("Awesome choice " + name + "!" " You will do well as a " + ChooseCharacter + "!")

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
    print("Your total is: $" + str(total))
else:
    print("You chose not to buy upgrades.")

print("Wonderful choice " + name + "! Your adventure starts now! We will meet again!")
```
Output: <br>
Hello Adventurer! Welcome to Aurora's Adventures!!! <br>
What is your name? <br>
Jasmine <br>
Hello Jasmine, we are happy to have you here! <br>
Choose a gamemode below you would like to play. <br>
easy mode, hard mode, extreme mode <br>
extreme mode <br>
You've chosen extreme mode. <br>
Jasmine, choose your character! Each character have different abilities. Check the options below. <br>
Healer, Fighter, Archaeology, Pilot <br>
Pilot <br>
Awesome choice Jasmine! You will do well as a Pilot! <br>
Would you like to buy upgrades? (Yes/No) <br>
Yes <br>
You chose to buy upgrades! You can buy up to 5 speed boost and 5 wacky coins each day. <br>
Choose your upgrades below! <br>
Speed boost, Wacky coins <br>
Speed boost and Wacky coins <br>
How many speed boost do you want? <br>
2 <br>
How many wacky coins do you want? <br>
2 <br>
Your total is: $12 <br>
Wonderful choice Jasmine! Your adventure starts now! We will meet again! <br><br>


# Part 3: If (True) Else (False) statements. Nested ifs
Using IF to control flow <br>
(Modified) Building a video game
```
print("Hello Adventurer! Welcome to Aurora's Adventures. Get Schwifty!!!")

name = input("What is your name?\n")

if name == "Rick":
    print("Get out of here Rick!!! You're going to ruin my........")
    exit()
if name == "Rick Sanchez":
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

print("Awesome choice " + name + "!" " You will do well as a " + ChooseCharacter + "!")

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

print("Wonderful choice " + name + "! Your adventure starts now! We will meet again!")
```


# Part 4: If Elif and Nested if
```
print("Hello Adventurer! Welcome to Aurora's Adventures. Get Schwifty!!!")

name = input("What is your name?\n")

if name == "Rick":
    suspiciousname = input("Are you Rick Sanchez?")
    if suspiciousname == "Yes":
        print("Get out of here Rick!!! You're going to ruin my........")
    else:
        print("Haha! You had me worried! You may enter!")
    exit()
if name == "Rick Sanchez":
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

print("Awesome choice " + name + "!" " You will do well as a " + ChooseCharacter + "!")

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

Options = "Tutorial, No tutorial"

Chooseoption = input("Would you like to do the tutorial?\n" + Options + "\n")

if Chooseoption == "Tutorial":
    print("Wonderful choice " + name + "! Let's enter the training room!")
elif Chooseoption == "No tutorial":
    print("Wonderful choice " + name + "! Your adventure starts now! We will meet again!")
```


# Part 5: logical Operators
```
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

if ChooseCharacter == "Archaeology":
    fact = input("A lion's roar can be heard up to eight kilometres away (Yes/No)\n")
    if fact == "Yes":
        print(LionRoar8KMFact)
    if fact == "No":
        print(LionRoarFact)
if not name == "Healer, Fighter, Pilot":
    print("Awesome choice " + name + "!" " You will do well as a " + ChooseCharacter + "!")

#The common way to use 'Not' is to use '!='
#Example 
 #if name != "Healer, Fighter, Pilot":
    #print("Awesome choice " + name + "!" " You will do well as a " + ChooseCharacter + "!")

#Boolean True or False
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

Options = "Tutorial, No tutorial"

Chooseoption = input("Would you like to do the tutorial?\n" + Options + "\n")

if Chooseoption == "Tutorial":
    print("Wonderful choice " + name + "! Let's enter the training room!")
elif Chooseoption == "No tutorial":
    print("Wonderful choice " + name + "! Your adventure starts now! We will meet again!")
```


# Part 6: list in Python
```
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

if ChooseCharacter == "Archaeology":
    fact = input("A lion's roar can be heard up to eight kilometres away (Yes/No)\n")
    if fact == "Yes":
        print(LionRoar8KMFact)
    if fact == "No":
        print(LionRoarFact)
if not name == "Healer, Fighter, Pilot":
    print("Awesome choice " + name + "!" " You will do well as a " + ChooseCharacter + "!")

#The common way to use 'Not' is to use '!='
#Example 
#if name != "Healer, Fighter, Pilot":
    #print("Awesome choice " + name + "!" " You will do well as a " + ChooseCharacter + "!")

#Boolean True or False
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

#Who to bring on the adventure.
Special_items = ["Magnifying glass", "Food", "Rope"]
import random

Guiders = "Harlow, Kai"
Harlow = Special_items[0]
Kai = Special_items[1]

#Tip: Reversed: You can select the last item on the list or any string of the list by using negative index
#Example: Kai = Special_items[-1] The selected item is will be 'Rope'
#Example: Kai = Special_items[-2] The selected item is will be 'Food'

print("Your adventure will be led by a guider! Guiders will randomly have one special items that will come in handy:" , Special_items ,)

Select_guiders = input("Choose a guider! Harlow: A loyal German Shepherd or Kai: The courageous lion. " "\n"  + Guiders + "\n")

if Select_guiders == "Harlow" or "Kai":
    Random_item = random.choice(Special_items)
    print(f"The guider will bring " + Random_item + "\n")

Options = "Tutorial, No tutorial"

Chooseoption = input("Would you like to do the tutorial?\n" + Options + "\n")

if Chooseoption == "Tutorial":
    print("Wonderful choice " + name + "! Let's enter the training room!")
elif Chooseoption == "No tutorial":
    print("Wonderful choice " + name + "! Your adventure starts now! We will meet again!")
```


# Part 7: Add stuff to Python list
```
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

if ChooseCharacter == "Archaeology":
    fact = input("A lion's roar can be heard up to eight kilometres away (Yes/No)\n")
    if fact == "Yes":
        print(LionRoar8KMFact)
    if fact == "No":
        print(LionRoarFact)
if not name == "Healer, Fighter, Pilot":
    print("Awesome choice " + name + "!" " You will do well as a " + ChooseCharacter + "!")

#The common way to use 'Not' is to use '!='
#Example 
#if name != "Healer, Fighter, Pilot":
    #print("Awesome choice " + name + "!" " You will do well as a " + ChooseCharacter + "!")

#Boolean True or False, YT 
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

Extra_items = ["Nunchucks", "Medkits", "Dental picks", "Tool kit"]

#Tip
#Concept: Methods
#Extra_items.append("Knife")
#Extra_items.append("Portable power")
#print(Extra_items)

Extra_items.extend(["Knife", "Portable power", "Matches", "Jacket", "Gloves"])

#Tip: Another code similar to 'extend'.
#Extra_items = Extra_items + ["Test", "Python"]
#print(Extra_items)

#Tip 2: Using 'inset'. You can add an string to the list either in the beginning, middle, or other.
#Example 1
#Extra_items.insert(0, "Test")
#print(Extra_items)

#Example 2 
#Extra_items.insert(-2, "Test 2")
#print(Extra_items)

items = input("Would you like to add extra items below? (Yes/No) \n")

if items.lower() == "yes":
    print("Here's the list of available extra items:", Extra_items)
    selected_items = input("Select the items you want (separate them with commas):\n")
    selected_list = [item.strip() for item in selected_items.split(",")]
    print(", ".join(selected_list) + " will be added to your inventory.")
if items == "No":
    print("You decided not to add extra items!")

#Who to bring on the adventure.
Special_items = ["Magnifying glass", "Food", "Rope"]
import random

Guiders = "Harlow, Kai"
Harlow = Special_items[0]
Kai = Special_items[1]

#Tip: Reversed: You can select the last item on the list or any string of the list by using negative index
#Example: Kai = Special_items[-1] The selected item is will be 'Rope'
#Example: Kai = Special_items[-2] The selected item is will be 'Food'

print("Your adventure will be led by a guider! Guiders will randomly have one special items that will come in handy:" , Special_items ,)

Select_guiders = input("Choose a guider! Harlow: A loyal German Shepherd or Kai: The courageous lion. " "\n"  + Guiders + "\n")

if Select_guiders == "Harlow" or "Kai":
    Random_item = random.choice(Special_items)
    print(f"The guider will bring " + Random_item + "\n")

Options = "Tutorial, No tutorial"

Chooseoption = input("Would you like to do the tutorial?\n" + Options + "\n")

if Chooseoption == "Tutorial":
    print("Wonderful choice " + name + "! Let's enter the training room!")
elif Chooseoption == "No tutorial":
    print("Wonderful choice " + name + "! Your adventure starts now! We will meet again!")
```


# Part 8: Delete stuff from Python Lists
```
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

if ChooseCharacter == "Archaeology":
    fact = input("A lion's roar can be heard up to eight kilometres away (Yes/No)\n")
    if fact == "Yes":
        print(LionRoar8KMFact)
    if fact == "No":
        print(LionRoarFact)
if not name == "Healer, Fighter, Pilot":
    print("Awesome choice " + name + "!" " You will do well as a " + ChooseCharacter + "!")

#The common way to use 'Not' is to use '!='
#Example 
#if name != "Healer, Fighter, Pilot":
    #print("Awesome choice " + name + "!" " You will do well as a " + ChooseCharacter + "!")

#Boolean True or False
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
 
Extra_items = ["Nunchucks", "Medkits", "Dental picks", "Tool kit"]

#Tip:
#Concept: Methods
#Extra_items.append("Knife")
#Extra_items.append("Portable power")
#print(Extra_items)

Extra_items.extend(["Knife", "Portable power", "Matches", "Jacket", "Gloves"])

#Tip: Another code similar to 'extend'.
#Extra_items = Extra_items + ["Test", "Python"]
#print(Extra_items)

#Tip 2: Using 'inset'. You can add an string to the list either in the beginning, middle, or other.
#Example 1
#Extra_items.insert(0, "Test")
#print(Extra_items)

#Example 2 
#Extra_items.insert(-2, "Test 2")
#print(Extra_items)

#Tip
#'.clear()' can remove everything from the list.
#Extra_items.clear()

#Tip
#'.remove("Gloves")' can remove specific strings on the list.
#Extra_items.remove("Gloves")
#Extra_items.remove("Jacket")

#Concept: Index
#Extra_items.pop(8) #This will remove the item listed under that number.
#Extra_items.pop(7)

#You can return the same data that was deleted. It's like a confirmation of what is being deleted.
#print(Extra_items.pop(2))
#print("I'm deleting this item: " + Extra_items.pop(2))

items = input("Would you like to add extra items below? (Yes/No) \n")

if items.lower() == "yes":
    print("Here's the list of available extra items:", Extra_items)
    selected_items = input("Select the items you want (separate them with commas):\n")
    selected_list = [item.strip() for item in selected_items.split(",")]
    print(", ".join(selected_list) + " will be added to your inventory.")
if items == "No":
    print("You decided not to add extra items!")

#Who to bring on the adventure.
Special_items = ["Magnifying glass", "Food", "Rope"]
import random

Guiders = "Harlow, Kai"
Harlow = Special_items[0]
Kai = Special_items[1]

#Tip: Reversed: You can select the last item on the list or any string of the list by using negative index
#Example: Kai = Special_items[-1] The selected item is will be 'Rope'
#Example: Kai = Special_items[-2] The selected item is will be 'Food'

print("Your adventure will be led by a guider! Guiders will randomly have one special items that will come in handy:" , Special_items ,)

Select_guiders = input("Choose a guider! Harlow: A loyal German Shepherd or Kai: The courageous lion. " "\n"  + Guiders + "\n")

if Select_guiders == "Harlow" or "Kai":
    Random_item = random.choice(Special_items)
    print(f"The guider will bring " + Random_item + "\n")

Options = "Tutorial, No tutorial"

Chooseoption = input("Would you like to do the tutorial?\n" + Options + "\n")

if Chooseoption == "Tutorial":
    print("Wonderful choice " + name + "! Let's enter the training room!")
elif Chooseoption == "No tutorial":
    print("Wonderful choice " + name + "! Your adventure starts now! We will meet again!")
```


-----------------------------------------------------------------------------------------------------------------------------------------------------------
# Part 9: Tuples
```
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
#if name != "Healer, Fighter, Pilot":
    #print("Awesome choice " + name + "!" " You will do well as a " + ChooseCharacter + "!")

#Boolean True or False
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

Extra_items = ["Nunchucks", "Medkits", "Dental picks", "Tool kit"]

#Tips
#Concept: Methods
#Extra_items.append("Knife")
#Extra_items.append("Portable power")
#print(Extra_items)

Extra_items.extend(["Knife", "Portable power", "Matches", "Jacket", "Gloves"])

#Tip: Another code similar to 'extend'.
#Extra_items = Extra_items + ["Test", "Python"]
#print(Extra_items)

#Tip 2: Using 'inset'. You can add an string to the list either in the beginning, middle, or other.
#Example 1
#Extra_items.insert(0, "Test")
#print(Extra_items)

#Example 2 
#Extra_items.insert(-2, "Test 2")
#print(Extra_items)

#Tip
#'.clear()' can remove everything from the list.
#Extra_items.clear()

#Tip
#'.remove("Gloves")' can remove specific strings on the list.
#Extra_items.remove("Gloves")
#Extra_items.remove("Jacket")

#Concept: Index
#Extra_items.pop(8) #This will remove the item listed under that number.
#Extra_items.pop(7)

#You can return the same data that was deleted. It's like a confirmation of what is being deleted.
#print(Extra_items.pop(2))
#print("I'm deleting this item: " + Extra_items.pop(2))

#Immutable = Not changable
#Mutable = You can change it
#You can't mute tuples
#You can mute list
#A list stores homogenous data.
#Example: Meat = ["Chicken", "Pork", "Steak"] 
#A tuple store heterogenous data. Data pertaining to specific variable, which is grouping different types of data.
#Example: Random = ("Red", "1000", "Black")

#Alist = ["Old", "Poison", "Pain"]
#Alist[1] = "Fire" 
#print(Alist)
#print(type(Alist))

#Atuple = ("Old", "Poison", "Pain")
#Atuple[3] = "Snow"
#print(Atuple)
#print(type(Atuple))

#A tuple is faster than a list

#import timeit

#List speed test
#print(timeit.timeit(stmt = '["Grapes", "Strawberry", "Blueberry", "Blackberry", 100, 50, 1]', number=3000000))

#Tuple speed test
#print(timeit.timeit(stmt = '("Chocolate", "Vanilla", "Walnut", "Almond", 1000, 500, 100)', number=3000000))

#You can unpack a tuple and assign it to multiple variables all at once. You can do the same for List.
#Adventurer = ("Unknown", 36, "Suspicious")

#(name, age, work) = Adventurer

#print(name)
#print(age)
#print(work)

#You do not need parentheses to make a tuple

#Test = 1,

#print(type(Test))

items = input("Would you like to add extra items below? (Yes/No) \n")

if items.lower() == "yes":
    print("Here's the list of available extra items:", Extra_items)
    selected_items = input("Select the items you want (separate them with commas):\n")
    selected_list = [item.strip() for item in selected_items.split(",")]
    print(", ".join(selected_list) + " will be added to your inventory.")
if items == "No":
    print("You decided not to add extra items!")

#Who to bring on the adventure.
Special_items = ["Magnifying glass", "Food", "Rope"]
import random

Guiders = "Harlow, Kai"
Harlow = Special_items[0]
Kai = Special_items[1]

#Tip: Reversed: You can select the last item on the list or any string of the list by using negative index
#Example: Kai = Special_items[-1] The selected item is will be 'Rope'
#Example: Kai = Special_items[-2] The selected item is will be 'Food'

print("Your adventure will be led by a guider! Guiders will randomly have one special items that will come in handy:" , Special_items ,)

Select_guiders = input("Choose a guider! Harlow: A loyal German Shepherd or Kai: The courageous lion. " "\n"  + Guiders + "\n")

if Select_guiders == "Harlow" or "Kai":
    Random_item = random.choice(Special_items)
    print(f"The guider will bring " + Random_item + "\n")

Options = "Tutorial, No tutorial"

Chooseoption = input("Would you like to do the tutorial?\n" + Options + "\n")

if Chooseoption == "Tutorial":
    print("Wonderful choice " + name + "! Let's enter the training room!")
elif Chooseoption == "No tutorial":
    print("Wonderful choice " + name + "! Your adventure starts now! We will meet again!")
```
