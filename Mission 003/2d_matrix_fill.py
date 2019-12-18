##
# Fills 2d matrix
# *finds valid pooling points
# *counts filled points
##

matrix4=[
[3,3,2,3,3,3,3],
[3,0,0,1,3,3,3],
[3,0,0,3,3,3,3],
[3,3,3,5,5,5,3],
[3,3,3,5,3,5,3],
[3,3,3,5,5,5,3],
[3,3,3,3,3,3,3]
         ]
# reads min max values of matrix
# returns dict key=matrix_value value=coordinates of all instances of that matrix_value
def read_levels(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    
    matrix_levels_coords={}
    for i in range(rows):
        for j in range(cols):
            if(matrix[i][j] not in matrix_levels_coords):
                matrix_levels_coords[matrix[i][j]]=[]
                matrix_levels_coords[matrix[i][j]].append((i,j))
            else:
                matrix_levels_coords[matrix[i][j]].append((i,j))
    return matrix_levels_coords 

# fill valid pooling points
# returns int count of filled points
def valid_pool_check_fill(matrix):
    
    row_len=len(matrix[0])-1
    col_len=len(matrix)-1

    levels=read_levels(matrix4) #read matrix levels
    keys=[]
    for i in levels:    #read keys in list
        keys.append(i)
    keys=sorted(keys)   #sort list min-max
    first=keys[0]       #get min key
    last=keys.pop()     #get max key
    
    volume=0            #track volume to get erosion

    
    #flood matrix levels from bottom -> up

    for k in range(first, last):
    #for k in range(first, last+1): # don't count last level
        
        checked_points=[]
        valid_pool_point=[]
        invalid_pool_points=[]
        for i in levels[k]: # i = coordinate tuple (x,y)
            valid=True
            if(i not in invalid_pool_points):

                #check if coordinate point is next to edge or invalid_pool_point
                #top left
                if((i[0]-1)<0 or (i[1]-1)<0 or (i[0]-1,i[1]-1) in invalid_pool_points):
                    valid=False
                    #print((i[0]-1,i[1]-1))

                #top top
                if((i[0]-1)<0 or (i[0]-1,i[1]) in invalid_pool_points):
                    valid=False
                    #print((i[0]-1,i[1]))
                    
                #top right
                if((i[0]-1)<0 or (i[1]+1)>row_len or (i[0]-1,i[1]+1) in invalid_pool_points):
                    valid=False
                    #print((i[0]-1,i[1]+1))
                    
                #left
                if((i[1]-1)<0 or (i[0],i[1]-1) in invalid_pool_points):
                    valid=False
                    #print((i[0],i[1]-1))
                    
                #right
                if((i[1]+1)>row_len or (i[0],i[1]+1) in invalid_pool_points):
                    valid=False
                    #print((i[0],i[1]+1))
                    
                #bottom left
                if((i[0]+1)>col_len or (i[1]-1)>row_len or (i[0]+1,i[1]-1) in invalid_pool_points):
                    valid=False
                    #print((i[0]+1,i[1]-1))
                    
                #bottom bottom
                if((i[0]+1)>col_len or (i[0]+1,i[1]) in invalid_pool_points):
                    valid=False
                    #print((i[0]+1,i[1]))
                    
                #bottom right
                if((i[0]+1)>col_len or (i[1]+1)>row_len or (i[0]+1,i[1]+1) in invalid_pool_points):
                    valid=False
                    #print((i[0]+1,i[1]+1))
                
                if(valid==True):
                    #coordinate point check passes
                    valid_pool_point.append(i)
                    checked_points.append(i)
                else:
                    #coordinate point check fails
                    #point doesn't pool
                    checked_points.append(i)

                    #list to track neighbouring points
                    points_to_check=[]
                    
                    #check if point has neighbors in same level
                    #topleft
                    if((i[0]-1,i[1]-1)  in levels[k]):
                        points_to_check.append((i[0]-1,i[1]-1))
                    #toptop
                    if((i[0]-1,i[1])    in levels[k]):
                        points_to_check.append((i[0]-1,i[1]))
                    #topright
                    if((i[0]-1,i[1]+1)  in levels[k]):
                        points_to_check.append((i[0]-1,i[1]+1))
                    #left
                    if((i[0],i[1]-1)    in levels[k]):
                        points_to_check.append((i[0],i[1]-1))
                    #right
                    if((i[0],i[1]+1)    in levels[k]):
                        points_to_check.append((i[0],i[1]+1))
                    #bottomleft
                    if((i[0]+1,i[1]-1)  in levels[k]):
                        points_to_check.append((i[0]+1,i[1]-1))
                    #bottombottom
                    if((i[0]+1,i[1])    in levels[k]):
                        points_to_check.append((i[0]+1,i[1]))
                    #bottomright
                    if((i[0]+1,i[1]+1)  in levels[k]):
                        points_to_check.append((i[0]+1,i[1]+1))

                    #if neighbours
                    if(len(points_to_check)>0):

                        
                        
                        #set neighbor point as invalid_pool_point
                        #neighbour points won't pool
                        while True:
                            templist=[] #list to track valid neighbours
                            checked=[]
                            for j in points_to_check:

                                #TODO set j invalid ?

                                
                                #print("points to check", points_to_check)

                                #check if neighbours are valid_pool_point
                                #if yes: remove from valid_pool_point,
                                #   add to invalid_pool_points,
                                #   add neighbour point to templist to track in next cycle
                                #if no: add to invalid_pool_points
                                #TL
                                tl=(j[0]-1,j[1]-1)
                                if(tl in levels[k]):
                                    if(tl in valid_pool_point):
                                        valid_pool_point.remove(tl)
                                        templist.append(tl)
                                    if(tl not in invalid_pool_points):
                                        invalid_pool_points.append(tl)
                                #TT
                                tt=(j[0]-1,j[1])
                                if(tt in levels[k]):
                                    if(tt in valid_pool_point):
                                        valid_pool_point.remove(tt)
                                        templist.append(tt)
                                    if(tt not in invalid_pool_points):
                                        invalid_pool_points.append(tt)                                    
                                #TR
                                tr=(j[0]-1,j[1]+1)
                                if(tr in levels[k]):
                                    if(tr in valid_pool_point):
                                        valid_pool_point.remove(tr)
                                        templist.append(tr)
                                    if(tr not in invalid_pool_points):
                                        invalid_pool_points.append(tr)
                                #L
                                l=(j[0],j[1]-1)
                                if(l in levels[k]):
                                    if(l in valid_pool_point):
                                        valid_pool_point.remove(l)
                                        templist.append(l)
                                    if(l not in invalid_pool_points):
                                        invalid_pool_points.append(l)
                                #R
                                r=(j[0],j[1]+1)
                                if(r in levels[k]):
                                    if(r in valid_pool_point):
                                        valid_pool_point.remove(r)
                                        templist.append(r)
                                    if(r not in invalid_pool_points):
                                        invalid_pool_points.append(r)
                                #BL
                                bl=(j[0]+1,j[1]-1)
                                if(bl in levels[k]):
                                    if(bl in valid_pool_point):
                                        valid_pool_point.remove(bl)
                                        templist.append(bl)
                                    if(bl not in invalid_pool_points):
                                        invalid_pool_points.append(bl)
                                #BB
                                bb=(j[0]+1,j[1])
                                if(bb in levels[k]):
                                    if(bb in valid_pool_point):
                                        valid_pool_point.remove(bb)
                                        templist.append(bb)
                                    if(bb not in invalid_pool_points):
                                        invalid_pool_points.append(bb)
                                #BR
                                br=(j[0]+1,j[1]+1)
                                if(br in levels[k]):
                                    if(br in valid_pool_point):
                                        valid_pool_point.remove(br)
                                        templist.append(br)
                                    if(br not in invalid_pool_points):
                                        invalid_pool_points.append(br)
                                
                            # if no new valid points are found, break loop
                            if(len(templist)<=0):
                                break
                            # else copy found points and continue neighbour checking
                            else:
                                points_to_check=templist
        #print stats for current level
        print("KEY(level): ",k)
        for i in matrix:
            print(i)
        volume+=len(valid_pool_point) # how many valid pooling points are found
        print("volume: ",volume)
        print("valid pools", sorted(valid_pool_point)) # valid points
        #print("invalid",sorted(invalid_pool_points))
        
        # update next level to matrix
        if(k+1 not in levels):
            levels[k+1]=[]

        # fill valid_pool_point points to matrix 'next level'
        # and update poolable point coordinates to level
        for n in valid_pool_point:
            matrix[n[0]][n[1]]+=1
            levels[k+1].append(n)
    return volume

print(valid_pool_check_fill(matrix4))


