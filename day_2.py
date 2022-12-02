'''
The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get if you were to follow the strategy guide.

For example, suppose you were given the following strategy guide:

A Y
B X
C Z

This strategy guide predicts and recommends the following:

    In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
    In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
    The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.

In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

A X - rock - 1
B Y - paper - 2
C Z - scissors - 3

'''

lines = []
score = 0
 

with open('day_2_puzzle.txt') as f:
    lines = f.readlines()

# for line in lines:
#     # Elf plays rock
#     if line[0] == "A":
#         if line[2] == "X":
#             score += 1 + 3
#         elif line[2] == "Y":
#             score += 2 + 6
#         elif line[2] == "Z":
#             score += 3

#     # Elf plays paper
#     elif line[0] == "B":
#         if line[2] == "X":
#             score += 1
#         elif line[2] == "Y":
#             score += 2 + 3
#         elif line[2] == "Z":
#             score += 3 + 6

#     # Elf plays scissors
#     elif line[0] == "C":
#         if line[2] == "X":
#             score += 1 + 6
#         elif line[2] == "Y":
#             score += 2 
#         elif line[2] == "Z":
#             score += 3 + 3


'''
--- Part Two ---

The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

X - lose
Y - draw
Z - win
'''


for line in lines:
    # Elf plays rock
    if line[0] == "A":
        if line[2] == "X":
            score += 0 + 3
        elif line[2] == "Y":
            score += 3 + 1
        elif line[2] == "Z":
            score += 6 + 2

    # Elf plays paper
    elif line[0] == "B":
        if line[2] == "X":
            score += 0 + 1
        elif line[2] == "Y":
            score += 3 + 2
        elif line[2] == "Z":
            score += 6 + 3

    # Elf plays scissors
    elif line[0] == "C":
        if line[2] == "X":
            score += 0 + 2
        elif line[2] == "Y":
            score += 3 + 3
        elif line[2] == "Z":
            score += 6 + 1
    
    
print(score)