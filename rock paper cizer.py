# Rock Paper Cizer

import random
name=input("Enter your name: " )
print("Welcome",name,"to our game")
print("Now you are the player 1\n")

r=int(input("Enter how many rounds do you want to play: " ))
print("")
round=1
player_win= 0
computer_win= 0
while round<=r:
    print(f"round: {round}")
    list = ["rock","paper","cizer"]
    choose=random.choice(list)
    n=input("Type one (rock/ paper/ cizer): " )
    print("Player2:",choose)
    if n !='rock' and n !='paper' and n !='cizer':
        print("Invalid!\nYou Lose")
    if n==choose:
        print("Result:- Match Draw")
        player_win += 1
        computer_win += 1
    elif n=="rock" and choose=="paper":
        print("Result:- You Lose")
        computer_win += 1

    elif n=="paper" and choose=="rock":
        print("Result:- You Win")
        player_win += 1
    elif n=="cizer" and choose=="paper":
        print("Result:- You Win")
        player_win += 1
    elif n == "paper" and choose == "cizer":
        print("Result:- You Lose")
        computer_win += 1
    elif n=="cizer" and choose=="rock":
        print("Result:- You Lose")
        computer_win += 1
    elif n=="rock" and choose=="cizer":
        print("Result:- you Win")
        player_win += 1

    print("")
    round+=1

if player_win > computer_win:
    print("congratulation you win this game",name)
elif player_win < computer_win:
    print("Oops you lose this game \nbetter luck next time",name)
else:
    print("match draw",name)
print("Match result:-")
print("   your score:",player_win)
print("   computer score:",computer_win)

