#!/usr/bin/python

import sys

# Write a function `rock_paper_scissors` to generate all of the possible
# plays that can be made in a game of "Rock Paper Scissors", given some
# input `n`, which represents the number of plays per round
# define a list with all of the possible Rock Paper Scissors plays
# define an inner recursive helper function that will perform the recursion
# while allowing us to preserve the outer function's function signature
# make an initial call to the recursive helper function to kick off the recursion

# define what the options are -> separated like in the test file line 8
options = [["rock"], ["paper"], ["scissors"]]

def rock_paper_scissors(n):
    # if n is equal to 0, return empty list -> from line 7 of the test file
    if n == 0:
        return [[]]

    # if n is equal to 1, return the options
    if n == 1:
        return options

    # set the output to an empty list
    output = []

    # set a list equal to the rock_paper_scissors n - 1
    listA = rock_paper_scissors(n - 1)
    # for loop -> the sub list in the list, return the output
    for subList in listA:
        # for loop -> action in the options, set new action equal to the sub
        # list + the action, then append the output with the new action
        for play in options:
            newPlay = subList + play
            output.append(newPlay)
    return output



if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')