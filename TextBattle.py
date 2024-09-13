#I'm going to attempt to make an rpg text fight thing
import random
import time
#First of all I'm adding a failsafe to prevent an infinite loop
failSafe = 0

#Player Variables
pHealth = 100
isBoosted = False
hasFleed = False #I know I spelt it wrong but I'm too lazy to change all the variable appearances.

#Attack Variable
attack = 0 

#Item Attributes
numPots = 3 #The number of potions that a given player has
numBoosts = 2 #The number of damage boosts the player has. (Lasts 1 turn)

#EnemyAttributes
eHealth = 100
isBracing = False
eChoice = 0
hasActed = False #This is another failsafe to avoid more overlap in Golem's attacks where he attacks and braces.

#Finally, I'm adding the variable that keeps track of the user's choice.
choice = 0

#Text at the beginning
print("\nA large golem appears in front of you. Roaring at you, you believe it wants to attack.")
print()

#---------------------------------------------------------------------------------------------------------------------------

#A while loop that repeats until either the pHealth or eHealth drops to 0 or less than 0
while pHealth > 0 and eHealth > 0 and hasFleed == False and failSafe != 10:
    print("What will you do?")
    print("1 - Attack || 2 - Use a healing potion || 3 - Use a damage boost potion || 4 - Flee || 0 - End Process")
    choice = int(input("Choice : "))

    print("----------------------------")
    print("[[PLAYER TURN]]")
    print("----------------------------")


    #Attack Chosen
    if choice == 1: 
        attack = random.randint(10,20)

        if isBoosted == True: #If the player is boosted...
            attack = attack * 2.5 #Multiply attack by 2.5x
            isBoosted = False

        if isBracing == True: #If Golem is bracing...
            attack = attack*.75
            print("Golem braced the attack! (-25% damage)")
            isBracing == False

        eHealth = eHealth - attack

        print("You attack for " + str(attack) + " damage.")
        if eHealth > 0:
            print("Golem has " + str(eHealth) + " health remaining.")
        attack = 0 #Setting attack back to 0, so that it doesnt just get larger and larger.

    #Potion of Healing Chosen
    elif choice == 2:
        if numPots <= 0:
            print("You reach into your bag and find no more potions left.")
        
        if numPots > 0:
            pHealth = pHealth + 25
            numPots = numPots - 1
            if pHealth > 100:
                pHealth = 100
            print("You successfully restore 25 health!")
            print("Current health is " + str(pHealth) + " HP.")
            print(str(numPots) + " potions remaining.")

    #Boost Chosen    
    elif choice == 3:
        if numBoosts > 0:
            isBoosted = True
            print("Successfully drank a damage boost potion. Next attack will be boosted!")
        elif numBoosts <= 0:
            print("You reach into your bag and find no more potions left.")

    #Flee chosen
    elif choice == 4:
        num = random.randint(1,100)
        if num <= 15:
            hasFleed = True
            print("You have fled! You lose your pride but you didn't die!")
            print("Weird Ending!!")
        elif num > 15:
            print("You tried to flee but fear overcame you. Failure.")

    elif choice == 0:
        print("Process ended")
        pHealth = 0
        eHealth = 0
        failSafe = 10

    else:
        print("You think you're funny? You just wasted a turn.")

    if eHealth <= 0 and failSafe != 10:
        print("The Golem has died! You win!!!")

    time.sleep(4)
    if hasFleed == False:
        print("----------------------------")
        print("[[ENEMY TURN]]")
        print("----------------------------")


#---------------------------------------------------------------------------------------------------------------------------
    
    #Now, here is the choice made by the ENEMY. They will either attack or brace
    #Attack - Deal damage to the player
    #Brace - Mitigate 20% of the next player attack
    if eHealth > 0 and pHealth > 0 and hasFleed == False and failSafe != 10: #if both are alive and the player hasnt fled...
        eChoice = random.randint(1,6)

        if eChoice <= 4 or isBracing == True and hasActed == False: #Attack if choice is 1-4, OR if he's already bracing.
            hasActed = True
            attack = random.randint(15,25) #Will do between 15 to 25 damage
            pHealth = pHealth - attack
            print("Golem chooses to attack!")
            print("Golem does " + str(attack) + " damage.")
            attack = 0

        if eChoice > 4 and hasActed == False:
            isBracing = True
            print("The golem braces for your next attack!!")

        hasActed = False #Remove the status that he has already attacked since his turn is over.

        time.sleep(2)
        print("----------------------------")
    #Here is the part where we check if the player has died.
    #Then it prints a message corrisponding to which entity is dead.
    if pHealth <= 0 and failSafe != 10:
        print("You have died. Game Over...")

    if pHealth > 0 and hasFleed == False:
        print("You have " + str(pHealth) + " health remaining.")
        print("----------------------------")
   
    #failSafe = failSafe + 1
    
