import random

number = random.randint(1,100)
attempt = 1
guess = int(input("Guess The Number: "))

while(True):
    if(guess>number):
        guess = int(input("Enter Another Number .This one is too big: "))
        attempt += 1

    elif(guess<number):
        guess = int(input("Enter Another Number .This one is too small: "))
        attempt += 1

    else:
        print(f" 'Yup' That's the Number. You guessed it Right in {attempt} attempts")
        break
