#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import codecs
import sys
from get_ability import *
import re
from mtgjson import CardDb
import fuckit

#create db
db = CardDb.from_file(db_file='AllSets.json')

#print("cmc,power,toughness,race,ability,color")
print("race,ability,color")

#read in our list of cards to check
with open('AllSets.json', encoding="utf-8") as f:
    lines = f.read()
    lines = json.loads(lines)
    #x = str(lines).encode("utf-8")
#getlist of cards
card_list = []

for set_thing in lines.keys():
    if set_thing == "UGL":
        continue

    if set_thing == "pMGD":
        continue
    for key in lines[set_thing]['cards']:
        #if "<class 'str'>" in key['name']:
        #    continue
        name =key['name'].encode('utf-8').decode('UTF-8')
        card = db.cards_by_name[name]


        if "Creature" == card.types[0]:
            try:
                if len(card.colors) == 1:
                    card_list.append(card)
            except: 
                pass

        
     

#get the values we want from the list of cards
def get_list(item):

    try:
        if item.power == "*":
            adjusted_power = "*"
        elif item.power == "0":
            adjusted_power = "0"
        elif "+" in item.power:
            value = item.power.split("+")
            adjusted_power = int(value[0])
        
        else:
            adjusted_power =  int(item.power) 

        if item.toughness == "*":
            adjusted_toughness = "*"
        elif item.toughness == "0":
            adjusted_toughness = "0"
        elif "+" in item.toughness:
            value = item.toughness.split("+")
            adjusted_toughness = int(value[0])
        

        else:
            adjusted_toughness = int(item.toughness)
        
        tf = ""
        if len(item.subtypes) == 2:
            tf = item.subtypes[1] 

        ability = get_ability(item)  
        
        #print(str(item.cmc) + "," + str(adjusted_power) + "," + str(adjusted_toughness) + "," + item.subtypes[0] + "," + ability + "," + item.colors[0])
        print(item.subtypes[0] + "," + ability + "," + item.colors[0])
    except:
        pass


for item in card_list:
    get_list(item)
