import random
def main():
    secretnumber = random.randint(1,10)
    while True:
        try:
            guess = int(input("Guess what number I'm thinking of between 1 and 10:"))
        except ValueError:
            print("Please enter your guess in numerical form")
            continue
        
        if guess > 0 and guess < 10:
            if guess == secretnumber:
                print("You got it!")
                break
            elif guess > secretnumber:
                print("Too high!")
            else:
                print("Too low!")
       
        else:
            print("I said between 1 and 10!") 

main()