name = input("Enter your name: ")
score = input("Enter your score: ")
if score.isdigit():
    score = int(score)
    with open("scores.txt", "r") as file:
        print("Scores in the file:")
        print(file.readlines())
        with open("scores.txt", "a") as file:
            file.write(f"{name} {score}\n")
else:
    print("Invalid score. Please enter a number.")

import os
filename = "scores.txt"
filepath = os.path.abspath(filename)
print(f"The file is saved at: {filepath}")