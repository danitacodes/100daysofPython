# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
both_names = name1.lower() + name2.lower()

t = both_names.count('t')
r = both_names.count('r')
u = both_names.count('u')
e = both_names.count('e')
first_number = t + r + u + e

l = both_names.count('l')
o = both_names.count('o')
v = both_names.count('v')
e = both_names.count('e')
second_number = l + o + v + e

love_score = int(str(first_number) + str(second_number))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
