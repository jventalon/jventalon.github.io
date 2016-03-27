# -*- coding: utf-8 -*-
"""
Created on 13-03-2016

@author: Justine Ventalon
"""

# Program parsing the csv file hskbis.csv containing chinese hsk vocabulary

import csv
import json

cleanedData = []
others = []

# read file in universal mode
with open("hsk.csv", "rU") as csvfile:
    hsk_vocabulary = csv.reader(csvfile, delimiter=",")
    
    #skip two first line
    next(hsk_vocabulary) 
    next(hsk_vocabulary)
    
    # for each line
    for word in hsk_vocabulary:
    
        item = {}
        item["level"] = word[0]
        item["simplified"] = word[1].decode("utf-8")
        item["pinyin_numbers"] = word[2]
        english = word[3].split("CL:")
        item["english"] = english[0].strip("; ").split("; ")
        if len(english) == 2:
            item["classifier"] = english[1].decode("utf-8")
        cleanedData.append(item)
    
# read file in universal mode
with open("hskbis.csv", "rU") as csvfile:
    hsk_vocabulary = csv.reader(csvfile, delimiter="\t")
    
    # for each line
    for word in hsk_vocabulary:
    
        item = {}
        item["simplified"] = word[0].decode("utf-8")
        item["traditional"] = word[1].decode("utf-8")
        item["pinyin_numbers"] = word[2]
        item["pinyin_tones"] = word[3].decode("utf-8")
        item["english"] = word[4].split("; ")
        found = False
        for key, value in enumerate(cleanedData):
            if value["simplified"] == item["simplified"]:
                found = True
                value["traditional"] = item["traditional"]
                value["pinyin_tones"] = item["pinyin_tones"]
                cleanedData[key] = value
        if not found:
            others.append(item)
    
# write file in binary mod
with open("hsk.txt", "wb") as outfile:
    json.dump(cleanedData, outfile)

# write file in binary mod
with open("others.txt", "wb") as outfile:
    json.dump(others, outfile)