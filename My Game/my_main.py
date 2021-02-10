import sys
import os
import time
import sys
import random

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

a = 1.7
b = 0.2
c = 0.08
z = 0.2
def wrong_choice():
    print("That option doesn't work, Try again.")

def GameOver():
    print("")
    print("\nGame Over.")
    x = input("Try again. (y/n) :")
    if x.lower() == "y":
        intro()
    elif x.lower() == "n":
        print("Thanks for playing.")
        exit
    else:
        wrong_choice()
        GameOver()
# Search cell for useful object
def option2():
    print("\n\nYou struggle to your feet to search the room.")
    print("Horrified by what you see, you closer inspect the room.\nThe walls are crumbling and you notice a loose brick, as you gain bravery, you approach one of the sketetons shackled to the wall.")
    print("You pick up the hand shackles from one of the skeleton and the arm breaks clean off.\nCRACK. \nThis startles you but reveals an iron shackle pin that you could use to pick the lock.\n")

    print ("(1) = Pull loose stone from wall")
    print ("(2) = Use the pin to pick the lock\n")
    opt2 = input("What would you like to do? : ")
    
    if opt2.lower() == "1":
        print("\nYou pull hard on the stone, your feet scrambling for grip on the hard stone")
        print("Floor, the stone breaks free and sends you tumbling back.")
        print("The hole reveals you are in a tower, soaring high above the clouds covering the town below.\n")
        print("You see no clear route to escape\n\n")
        option2()

    elif opt2.lower() == "2":
        print("\nYou struggle with the rusty lock but quickly and silently manage to disengage it.")
        print("After picking the lock, you slowly open the door and creep out of the cell.\n")
        print("A long and winding staircase takes you to the bottom of the tower, where you aproach an arched wooden door.\n\n")
        opt2_0()
    else:
        wrong_choice()
        option2()

def opt2_0():
    s1 = input ("(1) = Run and barge the door\n(2) = Silently open the door and creep in\n\nWhat would you like to do? : ")
    for cht in s1:
        sys.stdout.write(cht)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1.0)

# forcefully open the door
    if s1 == "1":
        s1prt = "\nYou run straight barging into the door and head straight into another dark stone room.\nA beautiful young woman in the distance notices your entrance,\nshe turns around and as you blink, you hear a screech.\nYou feel warm liquid running down your neck and as you open your eyes, you see a horrifying creature devouring your life force as you take your final breath."
        for cht in s1prt:
            sys.stdout.write(cht)
            sys.stdout.flush()
            time.sleep(c)
        time.sleep(1.0)
        GameOver()
        
#slowly open the door
    elif s1 == "2":
        print("\nAs you open the door, you see a beautiful woman walking down a corridor on your right")
        print("As you watch the woman walk down the corridor, she gracefully disappears.\n")
        opt2_1()
    else:
        wrong_choice()
        opt2_0()
#sneak after the woman
        
def opt2_1():
    s2 = input("(1) = Sneak after the woman\n(2) = Explore the room\n\nWhat would you like to do? : ")
    if s2 == "1":
        print("\nYou follow the corridor to where the woman disappeared")
        print("As you reach the end of the corridor you are faced with two giant doors,")
        print("one of the doors stained RED with BLOOD, the other frozen in ICE with GHOSTLY BLUE hue.")
        print("Behind the RED door you hear the frantic screams of a young woman")
        print("It sounds like she's crying out for help almost pleading")
        print("")
        opt2_1_1()

    elif s2 == "2":
        print("\nThe room contains nothing, other than a large glowing chest,\nupon opening the chest you find a shimmering black orb.")
        print("You hold the Orb of Antone")
        print("As you stare into it words appear: “Is your freedom worth your life? Take a chance to get out alive, but beware the cost is high!” ")
        #add dice roll
        opt2_2()

    else:
        wrong_choice()
        opt2_1()


    #pick between two doors
def opt2_1_1():
    door = input ("(1) = Enter the BLOODY RED door\n(2) = for the GHOSTLY BLUE door\n\nWhat would you like to do? : ")
    if door == "1":
        print("\nYou open the door and the monster looks you clear in the eye,\nno longer in her human form, she flies toward you.\nHer claws rip into your flesh as the life drains out of you")
        print("\nVampire: 'What a delicious snack, thanks beautiful'")
        GameOver()
    elif door == "2":
        print ("You open the door and are met by a friendly looking ghost. \n")
        print("""     .-----.
   .' -   - '.
  /  .-. .-.  |
  |  | | | |  |
   \\ \\o/ \\o/ /
  _/    ^    \\_
 | \\  '---'  / \\
 / /`--. .--`\\ \\
/ /'---` `---'\\ \\
'.__.       .__.'
    `|     |`
     |     |
     \\      '--.
      '.        `\\
        `'---.   |
              ) /
              \\/ """)
        
        opt2_1_2()
    else:
        wrong_choice()
        opt2_1_1()
#exit or weapons
def opt2_1_2():
    a = input("(1) = 'Would you like me to take you to the exit?'\nOr \n(2) = 'Would you like me to take you to the armoury to fight your own way out? : ")

    if a == "1":
        print("The mischievous young ghost takes you straight to the feasting room.\nAs soon as the door opens the monster looks you clear in the eye,\nno longer in her human form,\nshe flies toward you.\nHer claws rip into your flesh the life drains out of you")
        GameOver()
    elif a == "2":
        print("\nThe ghost leads you to the weapons room.\nThe room contains hundreds of bows, arrows, swords, shields and everything you could imagine!\nYou find some discarded rations and quickly eat them for strength,\nYou grab a magic Shield, Sword and wooden Spear.")
        print("As the ghost disappears he laughs and says “The exit is though the RED door HAHAHAHAHA” ")
        print("\nYou make your way back to the BLOODY RED door, calm your nerves, steel your will and plan your attack")
        opt2_1_3()
    else:
        wrong_choice()
        opt2_1_2()

def opt2_1_3():
    b = input("\n(1) = Sneak into the room\n(2) = Rush into the room\n\nWhat would you like to do? : ")
    if b == "1":
        print("\nYou push the door slowly open to reveal the beautiful young woman hunched over a lifeless body,\nher lips fixed to the neck of her victim.\nYou see the blood soaking her flowing white gown, it dawns on you as you see her draining the blood of this poor soul to feed herself")
        print("\nThe beautiful young woman is the monster!\n")
        print("Thankfully, she doesn’t appear to have noticed you enter")
        opt2_1_4()
    elif "2":
        print("\nYou burst through the bloody door at speed and startle the woman from her feed .\nShe rises into the air and reveals her scaly wings. \nWith the blink of an eye she has flown thrown you across the room.\nYou are injured but still alive")
        print("The creatures flies to the centre of the room and lets out a cry, ready to attack you once more")
        opt2_1_5()

        
#question 9
def opt2_1_4():
    c = input("\n(1) = Sneak to the exit\n(2) = Confront the woman\n\nWhat would you like to do? : ")
    if c == "1":
        print("With a deep breath and your back pressed hard against the wall,\nyou slowly make you way to the exit.\n\nAs you open the door the woman hears you,")
        print("instantly sprouting wings and screaming a high pitched wail.\nYou quickly close the door behind you and pull across a big steal bolt with all your remaining strength.")
        print("You run as fast as you can down the hill away from the castle.")
        print("\n\nFINALLY YOU ARE FREE AND SAFE")
        print("\n\nAs your mind comes to terms with finally escaping that trecherous hell hole, your mind flashes back to the screams you heard behind the RED DOOR.\nA tinge of guilt crosses your heart as your mind flashes back to the body the Vampire was devouring.\nAs you escaped you caught a glimpse of the body")
        print("The screams and pleas for help were indeed real and not a lure,\nthey belonged to a woman not much older than yourself.")
        print("As her final words haunt your mind, you can't help but wonder if you could have helped her")
        print("")
        print("Congratulations you win")
        print("")
        exit
    
    elif c == "2":
        s5 = "\nYou raise your sword to attack the woman but she hears the movement and notices you.\nShe lets out a high pitched scream as she sprouts wings and flies toward you."
        for cht in s5:
            sys.stdout.write(cht)
            sys.stdout.flush()
            time.sleep(z)
        time.sleep(1.0)
        opt2_1_5() 

#question 10.
def opt2_1_5():
    d = input("\n\n(1) = Attack the creature\n(2) = Defend the attack\n\nWhat would you like to do? : ")
    if d == "1":
        s2 = "With a mighty swing of the sword you manage to make contact and slash her wing.\n She lets out a scream more terrifying than before but is grounded and cannot fly"
        for cht in s2:
            sys.stdout.write(cht)
            sys.stdout.flush()
            time.sleep(z)
        time.sleep(1.0)
        opt2_1_6() 
    #qst 11
    elif d == "2":              
        s3 = "\nScreaming wildly, the creature flies at you with incredible speed,\nyou hold up your shield.\nShe hits the shield with incredible force,\nknocking you to your knees but injuring her greatly."
        for cht in s3:
            sys.stdout.write(cht)
            sys.stdout.flush()
            time.sleep(z)
        time.sleep(1.0)
        opt2_1_7() #qst 12

def opt2_1_6(): #qst 11
    s1 = "You run toward the grounded creature but see the exit at the other end of the room"
    for cht in s1:
        sys.stdout.write(cht)
        sys.stdout.flush()
        time.sleep(z)
    time.sleep(1.0)

    b = input("(1) = Run for exit\n(2) = Attack\n\nWhat would you like to do? : ")
    if b == "1":
        s2= "You run for the exit but the creature disappears from view.\nAs you approach the door you feel cold hands on your face,\nyou feel teeth sinking into your neck.\nThe light fades as you take your last breath.\n"
        for cht in s2:
            sys.stdout.write(cht)
            sys.stdout.flush()
            time.sleep(z)
        time.sleep(1.0)
        GameOver()

    elif b == "2":
        s3 = "You run at the beast thrusting your sword wildly but the creature disappears from view.\nAs you stand startled and confused,\nyou feel cold hands entangle you.\n You feel teeth sinking into your neck.\nThe light fades as you take your last breath."
        for cht in s3:
            sys.stdout.write(cht)
            sys.stdout.flush()
            time.sleep(z)
        time.sleep(1.0)
        GameOver()

def opt2_1_7():
    s1 = "\nAs the creature flies around in pain you decide whether to"
    for cht in s1:
        sys.stdout.write(cht)
        sys.stdout.flush()
        time.sleep(z)
    time.sleep(1.0)

    b = input("(1) = Run for the exit\n(2) = Ready yourself for another attack\n\nWhat would you like to do? : ")
    if b == "1":
        s2 =("You run for the exit but the creature disappears from view.\nAs you approach the door you feel cold hands on your face,\nyou feel teeth sinking into your neck.\n The light fades as you take your last breath.\nEnjoy your afterlife. You lose.")
        for cht in s2:
            sys.stdout.write(cht)
            sys.stdout.flush()
            time.sleep(z)
        time.sleep(1.0)
        GameOver()
    elif b == "2":
        print("You run to find a defensive position and ready your sword and shield.\nAs she flies toward you, you break cover and drive your sword directly through her chest. \n The beast screams but it is not dead, magic is still pumping through her veins")
        opt2_1_8() #qst 13

def opt2_1_8(): #qst 13
    s1 = "\nThe creature is clearly injured, writhing around on the floor."
    for cht in s1:
        sys.stdout.write(cht)
        sys.stdout.flush()
        time.sleep(z)
    time.sleep(1.0)
    print("")

    b = input("(1) = Run for the exit\n(2) = Finish the kill\n\nWhat would you like to do? : ")
    if b == "1" :
        s2 = "You run away from the beast at full speed the creature disappears from view.\nAs you stand startled and confused,\nyou feel cold hands entangle you.\n You feel teeth sinking into your neck.\nThe light fades as you take your last breath."
        for cht in s2:
            sys.stdout.write(cht)
            sys.stdout.flush()
            time.sleep(z)
        time.sleep(1.0)
        print()
        GameOver()
    elif b == "2":
        s3 = ("You approach the creature and drive the wooden spear directly through the heart. \nThe creature instantly regains form as a beautiful woman and begs for you to spare her life.")
        for cht in s3:
            sys.stdout.write(cht)
            sys.stdout.flush()
            time.sleep(z)
        time.sleep(1.0)
        print()
        print(" Do you Spare her life (1) / Finish the kill (2)")
        opt2_1_9() #qst 14

def opt2_1_9(): # qst 14
    b = " Do you Spare her life (1) / Finish the kill (2)"
    if b == "1":
        s1 = "As you turn for the exit, you hear the paranormal scream once more.\n The vampire is still alive and takes your life."
        for cht in s1:
            sys.stdout.write(cht)
            sys.stdout.flush()
            time.sleep(z)
        time.sleep(1.0)
        print()
        GameOver()
    elif b == "2":
        s2 = "You remove the stake and drive it once more hard into the chest.\n The woman let out a human cry.\n Concerned she may return,\n you remove the head with one strike of the sword.\n You rush toward to exit and get out alive!! "
        for cht in s2:
            sys.stdout.write(cht)
            sys.stdout.flush()
            time.sleep(z)
        time.sleep(1.0)
        print()
        print ("YOU WIN")

# search the room
#qst 6
def opt2_2():
    b = input("\n(1) = Roll a 6 to teleport home\n(2) = leave the orb and continue down the\n\nWhat would you like to do? : ")
    if b == "1":
        roll = random.randint(1,6)
        if roll == 6:
            s1 =("Congratuations, the orb has taken you to the exit!")
            for cht in s1:
                sys.stdout.write(cht)
                sys.stdout.flush()
                time.sleep(z)
            time.sleep(1.0)
            GameOver()
        elif roll == 1 or roll ==2 or roll ==3 or roll ==4 or roll ==5:
            s2 = ("I'm sorry, you are not so lucky, the orb cannot help you!")
            for cht in s2:
                sys.stdout.write(cht)
                sys.stdout.flush()
                time.sleep(z)
            time.sleep(1.0)
            opt2_1()
        # min = 1
        # max = 6
        # roll_again = "yes"
        # while roll_again == "yes" or roll_again == "y":
        #     print ("Rolling the dices...")
        #     print ("The values are....")
        #     print (random.randint(min, max))
        # roll_again = input("Roll the dices again?")
    elif b =="2":
        opt2_1()
    else:
        wrong_choice()
        opt2_2()




def option1():
    print("The screams get louder and closer")
    print("OH! NO! its a really big monster")
    print("ITS HURTS! SOMEONE HELP ME!")
    print("game over")
    playagain = input (" Whould you like to play again? yes or no ")
    if playagain == "NO" or playagain == "no":
        print ("Goodbye")
    elif playagain == "YES" or playagain == "yes":
        intro()
    else:
        wrong_choice()
        option1()

#Escape prision tower
def Choice():
    print("\n(1) = Force the door")
    print("(2) = Search the room")
    print("(3) = Go back to sleep\n")
    start = input("What would you like to do? : ").lower()

    if start.lower() == "1" :
        print("\n\nYou stand up, shaking from the realisation that you have been captured and run at the door.")
        print("BANG.\nThe door doesn’t budge but creates an almighty noise that bounces through the castle.")
        print("\nYou hear a scream like you have never heard before...")
        print("What is this monster… ")
        print("The screams get louder and closer")
        Choice()


    elif start.lower() == "2":
        option2()
        
    elif start.lower() == "3":
        print("Go back to sleep, sweet dreams.")
        print("     ######################")
        print("     |                    |")
        print("     |     HAHAHAHAHA     |")
        print("     |     HAHAHAHAHA     |")
        print("     |     HAHAHAHAHA     |")
        print("     |                    |")
        print("     ######################")
        Choice()
    else:
        wrong_choice()
        Choice()


### Players first decison : game starts here
def intro():
    print("You wake up on a cold stone floor.")
    time.sleep(a)
    print("Moonlight creeping through an iron barred window reveals skeletons chained to the walls.")
    time.sleep(a)
    print("The room is small and round with one arched door.\n")
    time.sleep(a)
    print("You hear a voice fill the room")
    time.sleep(a)
    name = input("What is your name? : ")
    time.sleep(a)
    print(f"\nIn fear you reply '{name.title()}'")
    time.sleep(a)
    print()
    print()

    intro_p1 = name.title() + ", I HOPE YOU SLEPT WELL \n HAHAHAHAHAHAHAHAHA"
    for cht in intro_p1:
        sys.stdout.write(cht)
        sys.stdout.flush()
        time.sleep(c)
    time.sleep(1.0)

    print()
    print()

    startgame = input("Would you like to start the game? (Y/N): ")
    if startgame == "n" or startgame == "N":
        print ("Maybe some other time. Bye for now...")
    elif startgame == "y" or startgame == "Y":
        print("Welcome to RUN!")
        Choice()
    else:
        wrong_choice()
        intro()


### Start Game - Enter name 



#Main function
intro()