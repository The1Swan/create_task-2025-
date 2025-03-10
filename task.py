import random

rock = "rock"
paper = "paper"
scissors = "scissors"
blaster = "blaster"

moves = [rock, paper, scissors, blaster]

def rock(player, game_master):
    if player == rock and game_master == scissors:
        print("player wins")
    elif player == rock and game_master == paper:
        print("game_master wins")
    elif player == rock and game_master == rock:
        print("tie")
    elif player == rock and game_master == blaster:
        print("game_master wins")

def paper(player, game_master):
    if player == paper and game_master == scissors:
        print("game_master wins")
    elif player == paper and game_master == paper:
        print("tie")
    elif player == paper and game_master == rock:
        print("player wins")
    elif player == paper and game_master == blaster:
        print("player wins")

def scissors(player, game_master):
    if player == scissors and game_master == scissors:
        print("tie")
    elif player == scissors and game_master == paper:
        print("player wins")
    elif player == scissors and game_master == rock:
        print("game_master wins")
    elif player == scissors and game_master == blaster:
        print("game_master wins")

def blaster(player, game_master):
    if player == blaster and game_master == scissors:
        print("player wins")
    elif player == blaster and game_master == paper:
        print("player wins")
    elif player == blaster and game_master == rock:
        print("player wins")
    elif player == blaster and game_master == blaster:
        print("tie")


def play_game():
    while True:
        player = input("What's your move? ")
        
        game_master = random.choice(moves(0,2))

        print("Game master chose" + game_master)

        if player == "rock":
            rock(player, game_master)
        elif player == "paper":
            paper(player, game_master)
        elif player == "scissors":
            scissors(player, game_master)
        elif player == "blaster":
            blaster(player, game_master)
        
        play_again = input("Do you want to play again? ")
        if play_again == "no":
            print("Thanks for playing!")
            break

play_game()
