x = 10
y = 5
print(x > y)
print(x == y)

age = input("enter age")
max = 100
min = 1
result = max >= min
if result == False:
    print("incorrect age")
else:
    print("age accepted")



name = input("what is your name")
age = input("what is your age")
score = input("what is your test score")
passed = 50
failed = 0
print("Hello", name, "age", age, "your score is", score)
result = passed >= failed
if result == True:
    print("congratulations")
else:
    print("you failed")