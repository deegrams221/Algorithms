#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    # Write a function that receives a recipe in the form of a dictionary, as well as all of the ingredients you have available to you, also in the form of a dictionary
    # keys will be the ingredient names, with their associated values being the amounts
    # recipe dictionary, these amounts will represent the amount of each ingredient needed for the recipe, while in the case of the ingredients dictionary, the amounts represent the amounts available to you
    # function should output the maximum number of whole batches that can be made for the supplied recipe using the ingredients available to you, as indicated by the second dictionary

    # create an empty list bc we dont know what will be in it yet
    pos_batches = []

    # create a for loop of item in recipe
    for item in recipe:
        # if the item is not in the ingredients return 0
        if item not in ingredients:
            return 0

        # if the item in the ingredients divided by the item in the recipe is greater than or equal to 1,
        if ingredients[item] // recipe[item] >= 1:

            # then pos_batches appends the item in the ingredients devided by the item in
              # the recipe to find the amount needed for the recipe
            pos_batches.append(ingredients[item] // recipe[item])

        # else, if there out of the item in the ingredients then return 0
        else:
            return 0

    # return the pos_batches min bc we need to know how many batches can be created
    return min(pos_batches)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 232, 'butter': 155, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))