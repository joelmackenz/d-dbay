import state
import random

def d3Roll():
    return random.randint(1,3)

def d4Roll():
    return random.randint(1, 4)

def d6Roll():
    return random.randint(1,6)

def d20Roll():
    return random.randint(1,20)

def getHypedBidders():
    roll = d20Roll() + state.modifier

    if roll <= 5:
        return -1
    elif 5 < roll < 15:
        return 0
    elif 15 <= roll < 20:
        return 1
    elif 20 <= roll < 25:
        return d4Roll() + 1
    elif 25 <= roll < 35:
        return d4Roll() + 2
    elif 35 <= roll:
        return d6Roll() + 3

def getItemStartingPrice():
    exactPrice = state.item_value * (state.item_percent * .01)
    return round(exactPrice, 2)

def getBiddersAttractedByPercent():
    if state.item_percent == 10:
        return d6Roll() + 1
    elif state.item_percent == 25:
        return d4Roll()
    elif state.item_percent == 50:
        return d4Roll() - 1

def getterminus_price():
    if state.rarity == "common":
        return round(state.item_value * .75, 2)
    elif state.rarity == "uncommon":
        return round(state.item_value * 1.1, 2)
    elif state.rarity == "rare":
        return round(state.item_value * d3Roll(), 2)