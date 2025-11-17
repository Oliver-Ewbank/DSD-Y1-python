token = 0
while token == 0
firstname = input("what is your first name")
lastname = input("what is your last name")
if len(firstname + lastname) > 20:
    print("error, input was to long")
if len(firstname + lastname) < 20:
    print("name accepted")
    break
print(firstname + lastname)
print("your name is", len(firstname + lastname))