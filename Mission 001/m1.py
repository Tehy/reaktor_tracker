
##
# Solves https://tracking-game.reaktor.com Mission 001
##

import base64
t=""
with open('transmission.txt','r') as f: # read data
    t=f.read()
for i in range(0,len(t)-16): # set for loop range
    j=i+16 
    t2=t[i:j] # read data in 16 byte chunks
    if(len(set(t2))==16): # if no repeating characters
        print(base64.standard_b64decode(t2).decode("utf-8")) # get flag
