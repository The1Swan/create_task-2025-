import random

moves = [rock, paper, scissors, blaster]
game_master = moves[random.randint(0,2)]

def rock():
    if player == rock and game_master == scissors:
        print("player wins")
    elif player == rock and game_master == paper:
        print("game_master wins")
    elif player == rock and game_master == rock:
        print("tie")

def paper():
    if player == paper and game_master == scissors:
        print("game_master wins")
    elif player == paper and game_master == paper:
        print("tie")
    elif player == paper and game_master == rock:
        print("player wins")

def scissors():
    if player == scissors and game_master == scissors:
        print("tie")
    elif player == scissors and game_master == paper:
        print("paper wins")
    elif player == scissors and game_master == rock:
        print("game_master wins")

def blaster():
    if player == blaster:
        print("player wins")

def play_game():
    player = True

    while player == True:
        player = input("whats your move?")
        if player == "rock":
            rock()
        elif player == "paper":
            paper()
        elif player == "scissors":
            scissors()
        elif player == "blaster":
            blaster()
        else:
            print("errror")
        
        play_again = input("Do you want to play again")
        if play_again == "no":
            break