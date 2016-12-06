#!/usr/bin/env python

import json
from pprint import pprint
import codecs
import sys
from get_ability import *
#create db
from mtgjson import CardDb
db = CardDb.from_file(db_file='AllSets.json')


#read in our list of cards to check
with open('list_of_cards') as f:
    lines = f.read().splitlines()


#getlist of cards
card_list = []
for item in lines:
    x = db.cards_by_name[item]
    card_list.append(x)

#get the values we want from the list of cards
for item in card_list:
    if item.power == "*":
        adjusted_power = "*"
    elif item.power == "0":
        adjusted_power = -1
    elif "+" in item.power:
        value = item.power.split("+")
        adjusted_power = int(value[0]) / int(item.cmc)
    
    else:
        adjusted_power =  int(item.power)/int(item.cmc) 

    if item.toughness == "*":
        adjusted_toughness = "*"
    elif item.toughness == "0":
        adjusted_toughness = -1
    elif "+" in item.toughness:
        value = item.toughness.split("+")
        adjusted_toughness = int(value[0]) / int(item.cmc)
    

    else:
        adjusted_toughness = int(item.toughness)/int(item.cmc)


    ability = get_ability(item)  


    #color(class)
    color = None
    if "Black" in item.colors[0]:
        color = 0
    elif "White" in item.colors[0]:
        color = 1
    elif "Blue" in item.colors[0]:
        color = 2
    elif "Green" in item.colors[0]:
        color = 3
    elif "Red" in item.colors[0]:
        color = 4
    else:
        print("OH NOES")

    print(adjusted_power, adjusted_toughness, item.subtypes[0], ability, color)



