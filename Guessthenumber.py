import random

def guess_the_number():
    number = random.randint(1, 100)
    attempts = 0

    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        guess = input("Take a guess: ")
        
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(guess)
        attempts += 1
        
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congrats! You guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    guess_the_number()
