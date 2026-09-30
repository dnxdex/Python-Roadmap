import random

rndm_num = random.randint(1, 100)
guess = 0

while rndm_num != guess:
    guess = int(input("Guess the number: "))
    if guess > rndm_num:
        print("Too high")
    elif guess < rndm_num:
        print("Too low")

print(f"You successfully guess the correct number {rndm_num}")