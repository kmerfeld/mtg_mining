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
print("cmc_rate,race,ability,color")

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
        cmc_rate = ""
        if "*" in item.power:
            cmc_rate = "*"
        else:
            cmc_rate =  (int(item.power) + int(item.toughness))/int(item.cmc)

        
        tf = ""
        if len(item.subtypes) == 2:
            tf = item.subtypes[1] 

        ability = get_ability(item)  
        
        #print(str(item.cmc) + "," + str(adjusted_power) + "," + str(adjusted_toughness) + "," + item.subtypes[0] + "," + ability + "," + item.colors[0])
        print(str(cmc_rate) + "," + item.subtypes[0] + "," + ability + "," + item.colors[0])
    except:
        pass


for item in card_list:
    get_list(item)
