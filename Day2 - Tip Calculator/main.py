#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the Tip Calculator")
total = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15?")
people = input("How many people to split the bill?")
givenTotal = float(total)
givenTip = int(tip)
givenPeople = int(people)
tipAmt = givenTotal *(givenTip /100)

calculation = (givenTotal + tipAmt) / givenPeople

newTotal = round(calculation, 2)

print(f"Each person should pay: ${newTotal}")