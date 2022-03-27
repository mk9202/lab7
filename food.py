"""
A module that represents the valid food types.

author: RITCS
author: << Maya Kaul >>
"""
from dataclasses import dataclass

# The set of valid food items
FOODS = {'beef', 'pork', 'chicken', 'onion', 'pepper', 'tomato'} # TOUPDATE
# The set of vegetables
VEGGIES = {'onion', "pepper", 'tomato'}   # TOUPDATE

# The calories for each food item (a dictionary, where 
# key = food name (string) and value = calories (int)
CALORIES = {
    'beef': 200,
    'chicken': 140,
    'pork': 100,
    'onion': 30,
    'pepper': 25,
    'tomato': 10
}


@dataclass(frozen=True)
class Food:
    name: str
    veggie: bool
    calories: int


def food_create(name):
    """
    Create a new food item.
    :param name: the name of the food
    :return: new Food object
    """
    food = Food(name, name in VEGGIES, CALORIES[name])

    return food
