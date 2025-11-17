energy_level = [12, 15, 18, 21, 24]
user_names = ["EarthySpace", "DevilCommandment", "RainbowRecruit"]
step_count = [7365, 3268, 5937, 9346, 11264]

print(energy_level)
print(user_names)
print(step_count)

length_list1 = len(energy_level) // 2
length_list2 = len(user_names) // 2
length_list3 = len(step_count) // 2

print(energy_level[0], energy_level[-1], energy_level[length_list1])
print(user_names[0], user_names[-1], user_names[length_list2])
print(step_count[0], step_count[-1], step_count[length_list3])

energy_level.append(input("what would you like to add to the list"))
user_names.append(input("what would you like to add to the list"))
step_count.append(input("what would you like to add to the list"))
print(energy_level)
print(user_names)
print(step_count)