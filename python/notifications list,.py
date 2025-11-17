notifications = [34, 28, 55, 40, 60, 22, 18]

print("Day1:", notifications[0], "Day2:", notifications[1], "Day3:", notifications[2], "Day4:", notifications[3], "Day5:", notifications[4], "Day6:", notifications[5], "Day7:", notifications[6])

print(max(notifications))
print(min(notifications))

total_notifications = notifications[0] + notifications[1] + notifications[2] + notifications[3] + notifications[4] + notifications[5] + notifications[6]
print(total_notifications)

total = notifications[0] + notifications[1] + notifications[2] + notifications[3] + notifications[4] + notifications[5] + notifications[6]
average = total / 3
print(average)

notifications.append(input("what would you like to add to the list"))
print(notifications)