import random

def start_game():
    target = random.randint(1, 65)
    lives = 3

    while lives > 0:
        guess = int(input("Guess the target number (1-65) : "))

        if guess == target:
            print("Congratulation your guess is correct!!\nGame Over.")
            lives -= 1
            break
        elif guess > target:
            print("Too High")
            lives -= 1
            print("Lives remaining: ", lives)
        elif guess < target:
            print("Too Low")
            lives -= 1
            print("Lives remaining: ", lives)
        else:
            print("Invalid input. Try again")
print("WELCOME TO NUMBER GUESSING GAME.")
start_game()
    
    