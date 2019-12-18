
##
# Solves https://tracking-game.reaktor.com Mission 002
##

import json
from statistics import *

with open('ppb.bin.log','r') as f:
    d=f.read().split(' ') # read binary
temp=""
for i in d:
    temp+=chr(int(i,2)) # convert binary to string

obj=json.loads(temp) # convert string to json
obj_len=len(obj)    # days
id_sums={}
data=[]
j=0
k=0
for k in range(0,obj_len):  # days
    for j in range(0,24):   # hours
        sum_per_day=0       # store daily sums
        key=obj[k]['readings'][j]['id']
        for i in obj[k]['readings'][j]['contaminants']:
            sum_per_day+=obj[k]['readings'][j]['contaminants'][i] # sum daily values
        id_sums[key]=sum_per_day # store sums key:value
        data.append(sum_per_day) # store sum data 

mean=mean(data) # mean value of sums data
stdev=stdev(data) # stdev of sums data
for i in id_sums: # get id of sum value that deviates from data values
    if(int(id_sums[i])>mean+stdev or int(id_sums[i])<mean-stdev):
        print(bytes.fromhex(i).decode('utf-8'))

    
