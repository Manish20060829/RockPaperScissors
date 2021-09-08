import random

list = ("rock", "paper", "scissors")

userscore = 0

computerscore = 0

while True:
    Computer = random.choice(list)
    Player = input("Choose you move!(Rock, Paper, Scissors): ").lower()
    if Player == Computer:
        print(f'Computer chose {Computer} its a tie')
    if Computer == "rock" and Player == "scissors":
        print(f'Computer chose {Computer} you loose')
        computerscore += 1
    if Computer == "paper" and Player == "rock":
        print(f'Computer chose {Computer} you loose')
        computerscore += 1
    if Computer == "scissors" and Player == "paper":
        print(f'Computer chose {Computer} you loose')
        computerscore += 1
    if Player == "rock" and Computer == "scissors":
        print(f'Computer chose {Computer} you win')
        userscore += 1
    if Player == "paper" and Computer == "rock":
        print(f'Computer chose {Computer} you win')
        userscore += 1
    if Player == "scissors" and Computer == "paper":
        print(f'Computer chose {Computer} you win')
        userscore += 1
    elif Player not in list:
        print("Sorry that is not a proper choice")
    else:
        asking_for_input = True
        while asking_for_input:
            choice = input('Do you want to play again(yes or no): ').lower()
            if choice == "no":
                break
            elif choice == "yes":
                asking_for_input = False
    if choice == "yes":
        print(f'Computer score: {computerscore}')
        print(f'User score: {userscore}')
    if choice == "no":
        print(f'Computer score: {computerscore}')
        print(f'User score: {userscore}')
        if userscore > computerscore:
            print("You had a better score. Congrats!")
            break
        if userscore < computerscore:
            print("The computer had a higher score. You lost!")
            break
        if userscore == computerscore:
            print("You and the computer have the same score!")
            break
