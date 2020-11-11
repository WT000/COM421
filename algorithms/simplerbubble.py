# This bubble sort is even more simplistic, the loop isn't altered
# by sorts that have already been completed
nlist = [5, 9, 2, 3, 6, 2, 1]

for i in range(len(nlist) - 1):
    for n in range(len(nlist) - 1):
        if (nlist[n] > nlist[n+1]):
            temp = nlist[n]
            nlist[n] = nlist[n+1]
            nlist[n+1] = temp
            
print(nlist)