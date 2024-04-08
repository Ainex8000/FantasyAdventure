#Fantasy Adventure Game - Xenia DeNoyer (xendenoy@uat.edu)
#This is a text based adventure game that will allow the user to choose their own path and make decisions that will impact their health.
#8/6/2023 - Project being reworked for POC. Will continue working for the final project. Attempted to separate text to make it more readable.
#8/12/2023 - Added combat system. Added global variables for player class and class ability. Added combat function. Added combat to scenario 2. Added time record function.

#Commands for developer:
#cls - clears the console

#Imports
import time

#Global Variables
health = 100
mana = 100
is_alive = True
armorClass = 10
playerClass = "None"
classAbility = "None"

#Functions
def save_game():
    #Saves the users inputs and writes data to a text file
    #Opens a file for writing and creates it if it doesn't exist
    file_obj = open("save_game.txt", "w")
    #Writes some stuff to the file
    file_obj.write("Saved Data: \n")
    #Close the file away
    file_obj.close()

def read_data():
    #Opens a file for reading
    file_obj = open("game_save.txt", "r")
    #Reads the file and displays it to the console
    print(file_obj.read())
    #Close the file away
    file_obj.close()

#Function to record time
def record_time(func):
    #This function records the time it takes to run the game
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Time to run: " + str(end - start))
    return wrapper

def scenario_1():
    #Global Variables
    global armorClass
    global playerClass
    global classAbility

    # This is the first scenario to choose a class
    print("\n\t*** Pick your class ***")
    print("\nYou have set off on your first adventure!")
    print("\nBefore we can continue any further, you need to pick a class")
    print("\nThe classes available are: Fighter, Cleric, Wizard, and Rogue")
    player_choice = input("\nWhich class will you choose? (Fighter, Cleric, Wizard, or Rogue): ")

    #Changes player stats based on class choice
    if player_choice == "Fighter":
        armorClass = 15
        playerClass = "Fighter"
        classAbility = "Action Surge"
        print("\nThe Fighter class is a melee class that uses weapons and armor to fight. They are the most versatile class and can be built in many different ways.")
        print("\nFighters have an armor class of 15 and have the ability to use Action Surge, allowing them to attack twice.")
    elif player_choice == "Cleric":
        armorClass = 18
        playerClass = "Cleric"
        classAbility = "Channel Divinity"
        print("\nThe Cleric class is a support class that uses magic to heal and buff allies. However, Clerics are also hard hitters with their mace.")
        print("\nClerics have an armor class of 18 and have the ability to use Channel Divinity, allowing them to use their god's power.")
    elif player_choice == "Wizard":
        armorClass = 12
        playerClass = "Wizard"
        classAbility = "Arcane Recovery"
        print("\nThe Wizard class is a ranged class that uses magic to attack enemies. They are the most powerful class, but also the most fragile.")
        print("\nWizards have an armor class of 12 and have the ability to use Arcane Recovery, allowing them to recover spell slots.")
    elif player_choice == "Rogue":
        armorClass = 14
        playerClass = "Rogue"
        classAbility = "Sneak Attack"
        print("The Rogue class is a versatile attacking at both close and far range. They are the most agile class and tend to be the sneakiest of the classes.")
        print("\nRogues have an armor class of 14 and have the ability to use Sneak Attack, allowing them to deal extra damage.")


    # Open file
    file_obj = open("game_save.txt", "a")
    # Write in users input
    file_obj.write("Scenario 1 input: " + player_choice + "\n")
    # Close file
    file_obj.close()

    print("\n\t*** You have chosen the " + player_choice + " class! ***")

def scenario_2():
    # This is the second scenario
    print("\n\t*** The Adventure Begins ***")
    print("\nYou can now begin your first adventure!")
    print("\nYou are walking down a path and come to a fork in the road.")
    print("\nYou can either go 1. Left or 2. Right.")
    player_choice = input("\nWhich way will you go? (1 or 2): ")

    # Open file
    file_obj = open("game_save.txt", "a")
    # Write in users input
    file_obj.write("Scenario 2 input: " + player_choice + "\n")
    # Close file
    file_obj.close()

    global health
    if player_choice == "1":
        print("\n\t*** The Left Path ***")
        print("\nYou have chosen to go left!")
        print("\nWhie walking you came across a chest!")
        print("\nYou open the chest and find a potion!")
        print("\nDrinking the potion gave you 10 HP!")
        health = health + 10
        print("\nYour health is now " + str(health) + "!")
    elif player_choice == "2":
        print("\n\t*** The Right Path ***")
        print("\nYou have chosen to go right!")
        print("\nWhile walking you came across a group of bandits!")
        print("\nBattle was unavoidable and you pursued combat!")
        #Insert combat opportunity here
        combat()
        health = health - 20
        print("\nYour health is now " + str(health) + "!")
    else:
        print("\n\t*** ERROR: Invalid Path ***")
        print("\nYou did not choose a valid option.")
        print("\nYou have been attacked by a group of bandits!")
        print("\nYou were unable to defend yourself.")
        health = health - 100

def scenario_3():
    # This is the third scenario
    print("\n\t*** The Tavern ***")
    print("\nYou continued on your path and came across a small town.")
    print("\nIt is rather late and best to retire to a tavern for the night.")
    print("\nYou enter the tavern and see a few people sitting around.")
    print("\nThere are a lot of colorful people here tonight, there is a bard playing music, a few people playing cards, and a few people drinking.")
    print("\nYou can either 1. Go to the bar and order a drink, 2. Go to the card table and play a game, or 3. Go to the bard and listen to the music.")
    player_choice = input("\nWhat will you do? (1, 2, or 3): ")

    # Open file
    file_obj = open("game_save.txt", "a")
    # Write in users input
    file_obj.write("Scenario 3 input: " + player_choice + "\n")
    # Close file
    file_obj.close()

    global health
    if player_choice == "1":
        print("\n\t*** The Bar ***")
        print("\nYou go to the bar and order a drink!")
        print("\nWhile drinking, you became acquainted with the few people drinking!")
        print("\nThey tell you about their recent tales and adventures!")
        print("\nYou gained some new friends, the Hidden Garden adventuring party!")
    elif player_choice == "2":
        print("\n\t*** The Card Table ***")
        print("\nYou go to the card table and play a game with the adventuring party, the Lucky Blighted!")
        print("\nYou played a few rounds and won a few coins!")
        print("\nUnfortunately, some of the members believed you were cheating and attacked you!")
        print("\nYou were able to defend yourself, but not without some injuries! The barkeep split up the fight")
        health = health - 10
        print("\nYour health is now " + str(health) + "!")
    elif player_choice == "3":
        print("\n\t*** The Bard ***")
        print("\nYou go to the bard and listen to the music!")
        print("\nWhile listening to the music, you became acquainted with the bard!")
        print("\nShe tells you about her recent tales and adventures through song and dance!")
        print("\nYou gained a new friend, the bard, Ronin Quickstep!")
    else:
        print("\n\t*** ERROR: Invalid Option ***")
        print("\nYou did not choose a valid option.")
        print("\nUnable to decide, you stood at the entrance of the tavern.")
        print("\nWhile standing there, another group of adventurers barged in, trampling you!")
        health = health - 100

def combat():
    #global variables
    global playerClass
    global classAbility
    global health

    # This is the combat system
    print("\n\t*** Combat ***")
    print("\nYou have entered combat!")
    print("\nYou can either 1. Attack, 2. Defend, or 3. Use " + classAbility +".")
    player_choice = input("\nWhat will you do? (1, 2, or 3): ")

    # Open file
    file_obj = open("game_save.txt", "a")
    # Write in users input
    file_obj.write("Combat input: " + player_choice + "\n")
    # Close file
    file_obj.close()

    #Combat options
    if player_choice == "1":
        print("\n\t*** Attack ***")
        #Checks player class and uses appropriate weapon
        if playerClass == "Fighter":
            print("\nYou attack the enemy with your sword!")
            print("\nYou deal 10 damage! Defeating your enemies!")
        elif playerClass == "Cleric":
            print("\nYou attack the enemy with your mace!")
            print("\nYou deal 10 damage! Defeating your enemies!")
        elif playerClass == "Wizard":
            print("\nYou attack the enemy with your magic!")
            print("\nYou deal 10 damage! Defeating your enemies!")
        elif playerClass == "Rogue":
            print("\nYou attack the enemy with your dagger!")
            print("\nYou deal 10 damage! Defeating your enemies!")
    elif player_choice == "2":
        print("\n\t*** Defend ***")
        print("\nYou defend yourself!")
        print("\nYou take 5 less damage!")
    elif player_choice == "3":
        #Checks player class and uses appropriate ability
        print("\n\t*** " + classAbility + " ***")
        print("\nYou use " + classAbility + "!")
        if playerClass == "Fighter":
            print("\nYou activated " + classAbility + ", allowing you to attack twice!")
            print("\nYou deal 20 damage! Defeating your enemies!")
        elif playerClass == "Cleric":
            print("\nYou activated " + classAbility + ", allowing you to use your god's power!")
            print("\nYou deal 25 damage! Defeating your enemies!")
        elif playerClass == "Wizard":
            print("\nYou activated " + classAbility + ", allowing you to recover spell slots!")
            print("\nYou deal 20 damage! Defeating your enemies!")
        elif playerClass == "Rogue":
            print("\nYou activated " + classAbility + ", allowing you to deal extra damage!")
            print("\nYou deal 15 damage! Defeating your enemies!")
    else:
        print("\n\t*** ERROR: Invalid Option ***")
        print("\nYou did not choose a valid option.")
        print("\nYou stood there, unable to decide what to do.")
        print("\nWhile standing there, the enemy attacked you!")
        health = health - 100

def get_player_name():
    # Gets and return player name
    player_name = input("Please pick a name for your character: ")
    # This returns the player's name to the main function
    return player_name

def display_intro(player_name):
    # Write an introduction that describes the user mission.
    print("\n\t*** Fantasy Adventure Game ***")
    print("\nWelcome " + player_name + " to the Game!")
    print("\nYour mission is to survive your first adventure!")
    print("\nThere will be many different events as you travel on your journey and you will have to choose what to do in each scenario.")
    print("\nCertain options will have different outcomes and can impact your health.")
    print("\nYou will be given a health bar and if your health drops to 0, you will die.")
    print("\nGood luck " + player_name + "!")
    print("\n\t*** Game Start ***\n")

    # Open file
    file_obj = open("game_save.txt", "a")
    # Write in players name
    file_obj.write("Players name: " + player_name + "\n")
    # Close file
    # file_obj.close()

    print("Today you will start your first adventure!")

def check_user_health():
    # If the user-health drops below 0 set isAlive to False
    global is_alive
    global health
    print("\nYour current health is " + str(health))
    if health <= 0:
        print("\nYou have met your end.")
        is_alive = False
    elif health >= 80:
        print("\nYou are feeling well!")
        is_alive = True
    else:
        print("\nYou're alive to say the least.")
        is_alive = True


@record_time
def main():
    # This is the main function that everything is run out of
    global is_alive
    global health
    play_again = True

    # This is the time delay
    for _ in range(1000000):
        pass

    print("\nWelcome to the game! This game is still in beta.")
    print("\nThe game is set to Easy difficulty by default. More options will be added later.\n")
    save_game()

    display_save = input("Would you like to display saved data? (y/n): ")
    if display_save == "y":
        read_data()
    else:
        print("\nYou choose not to display saved data.")

#This is the loop that runs the game
    while play_again == True:
        player_name = get_player_name()
        display_intro(player_name)
        scenario_1()
        check_user_health()
        if is_alive == True:
            scenario_2()
        check_user_health()
        if is_alive == True:
            scenario_3()
        check_user_health()
        if is_alive == True:
            print("\nYou made it through your first adventure! Congratulations, " + player_name + "!\n\n\n")
        else:
            print("\nYour adventure has come to an end, " + player_name + ".\n\n\n")
        print("\n\t*** Game Over ***\n\n")

        # Open file
        file_obj = open("game_save.txt", "a")
        # Write in players final health
        file_obj.write("Final health: " + str(health) + "\n")
        # Close file
        file_obj.close()

        # Ask the player if they would like to play again
        player_choice = input("\nWould you like to play again? (y/n): ")
        # Evaluate the player choice
        if player_choice == "y":
            play_again = True
            is_alive = True
            health = 100
        else:
            print("\nSee you later!")
            play_again = False


if __name__ == "__main__":
    # This checks if there is a main function and then runs it if there is
    main()