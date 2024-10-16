import random
def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 's', 'p'])

    if user == computer:
        print("It's a tie! play again.")
        return False
    elif (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') or (user == 's' and computer == 'p'):
        print("You won")
        return True
    print("You lose! play again.")
    return False

while True:
    if play():
        break



# print(play())