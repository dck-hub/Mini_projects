# number guessing game import random module to generate random number
import random

top_range = input("Insert the top range number: ")

if top_range.isdigit():
    top_range = int(top_range)
    if top_range <= 0:
        print("please type a number larger then 0 next time.")
        quit()

else:
    print("Please enter digit")
    quit()

random_num = random.randint(0, top_range)
# give the lower and upper limit that need to be generated

# print(random_num)
guesses = 0

while True:
    guesses += 1
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please enter number.')
        continue
    if user_guess == random_num:
        print("You've got it!!!")
        break
    elif user_guess > random_num:
        print("you are above the number!")
    else:
         print("you were below the number!")

print("You've got it in", guesses, "guesses.")
