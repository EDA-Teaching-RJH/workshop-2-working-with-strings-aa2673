
import random
def main():
    guess = int(input("Guess what number I'm thinking of between 1 and 10"))
    secretnumber = random.randint(1,10)
    if guess == secretnumber:
        print("You got it!")
    elif guess > secretnumber:
        print("Too high!")
    elif guess < secretnumber:
        print("Too low!")
    else:
        print("Enter a valid guess please")

main()