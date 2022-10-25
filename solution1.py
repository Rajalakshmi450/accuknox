#solution without using Data Frames
import pandas as pd
import math
from collections import OrderedDict
from collections import Counteren
#find duplicates in the file and if yes raise error
counts = { }    
with open("logger.txt") as f: 
    for line in f: 
        stripline = line.strip() 
        myhash = hash(stripline)    
        if myhash: 
            if myhash in counts:    
                counts[myhash] = counts[myhash]+1                 
            else: 
                counts[myhash] = 1  
for myhash in counts: 
    if counts[myhash] > 1: 
        errstr="Found eater_id with the same foodmenu_id more than once"
        raise TypeError(errstr)

#get foodmenu_id to a list
food=[x.split(' ')[1] for x in open('logger.txt').readlines()]
food=list(map(lambda s: s.strip(), food))

#sort the count of each elements in the list
food_set=set(food)
count={x:food.count(x) for x in food_set}
sorted_count=dict(sorted(count.items(), key=lambda item: item[1], reverse=True))

#top 3 food_id with comma separated
food_id =[v for v in sorted_count.keys()][:3]
output=','.join([str(elem) for elem in food_id])
print(output)

