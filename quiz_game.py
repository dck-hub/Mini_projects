# Creating a simple quiz game algorithm

print("Welcome to the Quiz game!!!")

# check user wants to play game

play_game = input("Do you want to play the game: ").lower()
if play_game != "yes":
    quit()

print("Okay, Let's play: )")
score = 0

# Add three questions for the give marks

ans = input("what is IT stand for? ")
if ans == "Information Technology":
    print("Correct")
    score += 1
else:
    print("Incorrect")

ans2 = input("what is AWS stand for? ")
if ans2 == "Amazon Web Services":
    print("Correct")
    score += 1
else:
    print("Wrong")

ans3 = input("what is IP stand for? ")
if ans3 == "Internet Protocol":
    print("Correct")
    score += 1
else:
    print("wrong")

# print the final score

print("Your have " + str(score) + " score of 3.")
print("Your have " + str((score/3) * 100) + "%.")
