import random

secret_number = random.randint(1,10)

print("Welcom to the Number Guessing Game.")
print("Guess a number between 1 and 10.")

while True:
    guess = int(input("Enter your number"))

    if guess < 1 or guess >10:
        print("Enter a number between 1 and 10")
        continue

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess < secret_number:
        print("Too low. Try again.")

    else:
        print("Too high. Try again.")

else:
    print("Game Over")


import random

secret_number = random.randint(1,10)

attempts = 3

print("Welcom to the Number Guessing Game.")
print("Guess a number between 1 and 10.")

while attempts > 0:
    guess = int(input("Enter your number"))

    if guess < 1 or guess >10:
        print("Enter a number between 1 and 10")
        continue

    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break
    elif guess < secret_number:
        print("Too low. Try again.")

    else:
        print("Too high. Try again.")

    attempts -=1
    print("Attempte remainig:",attempts)

else:
    print("Better luck next time. The secret_number was: ",secret_number)
  


number = int(input("Enter a number for which they want to generate a multiplication table"))

for i in range(1,11):
    result = number * i
    print(number, "x", i, "=", result)

def calculate_bmi(weight, height):
    bmi = weight / (height**2)
    return bmi

weight = float(input("Enter your weight in kg:"))
height = float(input("Enter your height in meters:"))

bmi = calculate_bmi(weight, height)

print("Your bmi is:", round(bmi, 2))
    
