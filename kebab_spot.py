"""
A dataclass that represents "spots" on the skewer and functions that work
with it.

author: RITCS
author: << Maya Kaul >>
"""

from dataclasses import dataclass
from typing import Union
from food import Food


@dataclass
class KebabSpot:
    """
    Class: KebabSpot
    Description: This class is used to represent an individual
        spot on the skewer.  Each spot contains a Food 'item',
        and a reference to the 'next' spot.
    """
    item: Food
    next: Union[None, 'KebabSpot']


def spot_create(item, next):
    """
    Create a new food item spot on the skewer
    :param item (Food): new food item
    :param next: next spots
    :return: new spot
    """
    spot = KebabSpot(item, next)
    return spot

def spot_name(spot):
    """
    Return the name of the food item in this spot.
    :param: spot (KebabSpot): the current spot on the skewer
    :return: food name
    """
    spot = spot.item.name
    return spot

def spot_size(spot):
    """
    Return the number of elements from this KebabSpot instance to the end
    of the skewer.
    :param: spot (KebabSpot): the current spot on the skewer
    :return: the number of elements (int)
    """
    count = 0
    while spot is not None:
        count += 1
        spot = spot.next

    return count


def spot_has(spot, name):
    """
    Return whether there are is a food item from this spot to the end of
    the skewer.
    :param: spot (KebabSpot): the current spot on the skewer
    :param name: the name (string) being searched for.
    :return True if any of the spots hold a Food item that equals the
    name, False otherwise.
    """
    while spot is not None:
        if name == spot:
            return True
        else:
            return False


def spot_string_em(spot):
    """
    Return a string that contains the list of items in the skewer from
    this spot down, with a comma after each entry.
    :param: spot (KebabSpot): the current spot on the skewer
    :return A string containing the names of each of the Food items from
    this spot down.
    """

    lst_str = ""
    next = spot
    while spot is not None:
        next = spot.item.name
        print(spot)
        lst_str = lst_str + str(next)
        print(lst_str)
        spot = spot.next
        print(spot)
    if spot is not None:
        lst_str = lst_str + ", "

    return lst_str


def calories(spot):
    """
    :Description: This functions returns the sum of the calories in the kebab
    :Precondition: the spot needs to be the spot on the kebab
    :Postcondition: it updates the next spot
    :param: spot is the dataclass
    :return: the sum
    """
    spot = spot.skewer.top
    next = spot
    sum = 0
    while spot is not None:
        next = spot.item.calories
        sum += next
        next = spot.next
    return sum


def vegan(spot):
    """
     :Description: This functions returns whether the kebab is vegan or not
     :Precondition: the spot needs to be the spot on the kebab
     :Postcondition: it updates the next spot
     :param: spot is the dataclass
     :return: the next
     """
    spot = spot.skewer.top
    next = spot
    while spot is not None:
        next = spot.item.veggie
        if spot is True:
            spot = spot.next
        return next