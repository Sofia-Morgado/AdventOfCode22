'''
This list represents the Calories of the food carried by five Elves:

    The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
    The second Elf is carrying one food item with 4000 Calories.
    The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
    The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
    The fifth Elf is carrying one food item with 10000 Calories.

In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
'''

lines = []
max_calories_1 = 0
max_calories_2 = 0
max_calories_3 = 0
calories = 0

with open('day_1_puzzle.txt') as f:
    lines = f.readlines()

for line in lines:
    if line == '\n':
        if(max_calories_1 < calories):
            max_calories_3 = max_calories_2
            max_calories_2 = max_calories_1
            max_calories_1 = calories
        
        elif(max_calories_2 < calories):
            max_calories_3 = max_calories_2
            max_calories_2 = calories

        elif (max_calories_3 < calories):
            max_calories_3 = calories
        
        calories = 0
        continue

    calories += int(line);
    
    
print(max_calories_1 + max_calories_2 + max_calories_3)