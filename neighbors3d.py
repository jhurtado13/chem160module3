from random import choice
n=100
count = 0
nocc = 0
list3d=[[[choice((0,1)) for x in range(n)] for y in range(n)]for z in range(n)]
for x in range(1,n-1):
    for y in range(1,n-1):
        for z in range(1,n-1):
            if list3d[x][y][z]==1:
                nocc+=1
                neigh=list3d[x-1][y][z]+list3d[x+1][y][z]+list3d[y-1][x][z]\
                +list3d[y+1][x][z]+list3d[z+1][x][y]+list3d[z-1][x][y]
                if neigh > 2:
                    count+=1
print("Fraction with more than two neighbors:",count/nocc)