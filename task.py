import random
game_master_moves = ['rock', 'paper', 'scissors']

def decide_winner(player, game_master):
    winner = ''

    if player == "rock" and game_master == 'paper':
        winner = 'Game Master'
    elif player == "rock" and game_master == 'scissors':
        winner = 'player'
    elif player == "rock" and game_master == 'rock':
        winner = 'nobody'
   
    elif player == "paper" and game_master == 'paper':
        winner = 'nobody'
    elif player == "paper" and game_master == 'scissors':
        winner = 'Game Master'
    elif player == "paper" and game_master == 'rock':
        winner = 'player'
   
    elif player == "scissors" and game_master == 'paper':
        winner = 'player'
    elif player == "scissors" and game_master == 'scissors':
        winner = 'nobody'
    elif player == "scissors" and game_master == 'rock':
        winner = 'Game Master'
    
    elif player == "blaster":
        winner = 'player'
    
    else:
        winner = 'nobody'
        print("Error, no winner")

    print(f'The winner is: {winner}')

def play_game():
    while True:
        player = input("What's your move? ")
        
        game_master = random.choice(game_master_moves)

        print(f"Game master choses {game_master}")

        decide_winner(player, game_master)

        play_again = input("Do you want to play again? ")
        if play_again.lower() == "no":
            print("Thanks for playing!")
            break
        elif play_again.lower() == "yes":
            continue
        else:
            print("Not Aplicable")
            break

play_game()
