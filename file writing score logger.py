name = input("Enter your name: ")
score = input("Enter your score: ")
with open("scores.txt", "a") as file:
    file.write(f"{name} {score}\n")

with open("scores.txt", "r") as file:
    print("Scores in the file:")
    print(file.readlines())

import os
filename = "scores.txt"
filepath = os.path.abspath(filename)
print(f"The file is saved at: {filepath}")