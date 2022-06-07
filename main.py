import random

CPU = 0
Player = 0

def Choose_Option():
    user_choice = input ("PICK ONE OF THE FOLWOING, R, P, S:" )
    if user_choice in ["Rock", "rock", "R", "r"]:
        user_choice = "Rock"
    elif user_choice in ["Paper", "paper", "P", "p"]:
        user_choice = "Paper"
    elif user_choice in ["Scissors", "scissors", "S", "s"]:
        user_choice = "Scissors"
    
    else:
        print("I dont understand please try again")
        Choose_Option()
    return user_choice


def Computer_Option():
    computer_choice = random.randint(1,3)
    if computer_choice == 1:
        computer_choice = "Rock"
    elif computer_choice == 2:
        computer_choice = "Paper"
    elif computer_choice == 3:
        computer_choice = "Scissors"
    return computer_choice


while True:
    user_choice = Choose_Option()
    computer_choice = Computer_Option()
    print("")

    if user_choice  == "Rock":
        if computer_choice == "Rock":
            print ("You tied!")
            pass
        elif computer_choice == "Paper":
            print ("You lost!")
            CPU+=1
        elif computer_choice == "Scissors":
            print ("You won!")
            Player+=1

    if user_choice == "Paper":
        if computer_choice == "Rock":
            print ("You won!")
            Player+=1
        elif computer_choice == "Paper":
            print ("You tied!")
            pass
        elif computer_choice == "Scissors":
            print ("You lost!")
            CPU+=1


    if user_choice == "Scissors":
        if computer_choice == "Rock":
            print ("You lost!")
            CPU+=1
        elif computer_choice == "Paper":
            print ("You won!")
            Player+=1
        elif computer_choice == "Scissors":
            print ("You tied!")
            pass

    print("Player("+str(user_choice)+") : CPU("+str(computer_choice)+")")
    print( "Player (" +str(Player) +")")
    print( "CPU ("+str(CPU) +")")