print('''
  [4;5m***     *** [0m
 [4;5m**   ** **   ** [0m
[4;5m*       *       * [0m
[4;5m*               * [0m
 [4;5m*     LOVE    * [0m
  [4;5m**         ** [0m
    [4;5m**     ** [0m
      [4;5m** ** [0m
        [4;5m* [0m
''')

print("Welcome to Fantasy Island.")
print("Your task is to find love.")

first_part = input("You have arrived at Fantasy Island. You have a choice to go to the left or right side of the island. What say you? Type 'left' or 'right' \n").lower()


#Conditional
if first_part == 'left':
  second_part = input("You arrive at this beautiful stream. You see another island in the distance. Do you swim to it or wait for a boat? Type 'swim' or 'boat' \n").lower()
  if second_part == 'swim':
    third_part = input("You've made it to the tiny island. There are three doors to choose from. Red, Blue, and Green. Which one you choosing? Type 'red', 'blue', or 'green'. \n").lower()
    if third_part == 'blue':
      print("You've found the love of your life.")
    else:
      print("You chose the wrong door. Game Over!")
  else:
    print("You waited too long for a boat and died from sun exposure. Game Over!")
else:
  print("You've chosen the path of lonely hearts. Game Over!")