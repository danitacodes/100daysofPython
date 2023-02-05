# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
#takes names and creates a list
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#finds random item in list
random_name = random.randint(0, len(names) - 1)

#is the name of the person at the random index
name = names[random_name]

print(f"{name} is going to buy the meal!")