from random import randint
t = ["Rock","Paper","Scissors"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
     if player == computer:
         print("Tie")
    elif player == "Rock":
        if computer == "paper":
            print("you lose!",computer , "covers", player)
        else:
            print("You win!",player,"smashes",computer)
    elif player == "paper":
        if computer == "Scissors":
            printf(" you lose!",computer,"cut", player)
        else:
            print("you win!",player, "covers",computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("you lose ...",computer,"smashes", player)
        else:
            print("You win!",player,"cut",computer)
        else:
            print("that's not a valid play. Check your spelling")        
    #player was set to True , but we want it to be False so the loop continues
    player = False
    computer =t[randint(0,2)]
