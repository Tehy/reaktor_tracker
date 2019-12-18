
##
# Solves https://tracking-game.reaktor.com Mission 003
##

import json
from statistics import *

with open('flood.txt','r') as f:
    d=f.read()
obj=json.loads(d)

region_changes=[] # store read new region

for j in obj['regions']:
    for k in j['readings']:

        data=k['reading']   # 1d matrix data
        temp=data.copy()    # array to keep track of remaining values
        local_max=data[0]   # store current local max
        pooling=0           # store poolable pool volume
        volume=0            # store total pool volumes

        #read matrix data
        for i in range(len(data)):
            temp.pop(0)
            if data[i]>=local_max:  # update localmax
                local_max=data[i]
            elif data[i]<local_max: # start pooling
                try:
                    if data[i]<=max(set(temp)): # if pool possible
                        if(i>0):    # exclude edge case
                            if(local_max<max(set(temp))):   # if local_max < max remaining
                                pooling=(local_max-data[i]) # fill to local_max
                                volume=volume+pooling
                            else:   # local_max >= remaining values
                                pooling=(max(set(temp))-data[i]) # fill to max remaining value
                                volume=volume+pooling
                except ValueError as e:
                    e
            else:                   
                local_max=data[i]   # update localmax
        if j['regionID'] not in region_changes: # store first volume value to last_vol
            region_changes.append(j['regionID'])
            last_vol=volume
        else:   # calculate day-to-day volume changes in region
            if(volume-last_vol)>1000:   # if change > 1000
                print(k['readingID'])   # print readingID
            last_vol=volume             # udpate last_vol value
