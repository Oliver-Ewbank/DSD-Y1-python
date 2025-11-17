screen_times = [120, 95, 140, 160, 80, 100, 200]

print(screen_times[2])

total = screen_times[0] + screen_times[1] + screen_times[2]
average = total / 3
print(average)

screen_times[-1] = int(input("what would you like the new value to be"))
print(screen_times)

print(max(screen_times))
print(min(screen_times))