with open("scores.txt", "a") as file:
    file.write("oliver 100\n")

with open("scores.txt", "r") as file:
    lines = file.read
    linecount = file.readlines()
    print("There are " + str(len(linecount)) + " lines in the file.")

    import os

filename = "scores.txt"
filepath = os.path.abspath(filename)
print(f"The file is saved at: {filepath}")