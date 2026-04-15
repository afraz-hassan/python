import random

print("Enter your name: ", end="")
name = str(input())
len = len(name)

print("Well, " + str(name) +", I am thinking of a number between 1 and 100.")
print("Take a guess: ", end="")

random_num = random.randint(1,100)

score = 1
guess = 0

while guess != random_num:
    try:
        guess = int(input())
    except ValueError:
        print("Please enter a valid number: ", end="")
        continue

    if guess < int(random_num/2):
        print("\nyour guess is too low, try a higher number: ", end="")
        score += 1
        continue
    elif guess > int(random_num*2):
        print("\nyour guess is too high, try a lower number: ", end="")
        score += 1
        continue
    elif guess < int(random_num):   
        print("\nyour guess is a bit low, try a higher number: ", end="")
        score += 1
        continue
    elif guess > int(random_num):   
        print("\nyour guess is a bit high, try a lower number: ", end="")
        score += 1
        continue
    else:
        print("\nGood job, " , name,"! you guessed my number in ", score, "tries")