print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
answer1 = input(
    "You're on a crossroad. Where do you want to go? Type  \"left \" or  \"right \" \n"
)
if answer1.lower() == "right" or answer1.lower() != "left":
    print("You fell into a hole. Game over.")
else:
    answer2 = input(
        "You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n"
    )
    if answer2.lower() == "swim" or answer2.lower() != "wait":
        print("You get attacked by an angry shark. Game over.")
    else:
        answer3 = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which colour do you choose?\n"
        )
        if (answer3.lower() == "red"):
            print("It's room full of fire. Game over.")
        elif (answer3.lower() == "blue"):
            print("Eaten by beasts. Game over.")
        if (answer3.lower() == "yellow"):
            print("You Win!")
        else:
            print("Game over.")

#https://www.draw.io/lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20#Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx#2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
