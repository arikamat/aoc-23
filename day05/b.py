from math import sqrt
def findloc(seednum,arr):
    curr = seednum
    for i in arr:
        for idx in range(len(i)):
            start = i[idx][0]
            end = i[idx][0]+i[idx][2]
            if curr in range(start,end):
                curr = (curr-i[idx][0] + i[idx][1])
                break
    return curr
f = open("sample","r")
f= open("in","r")
lines = f.readlines()

seeds = list(map(int,lines[0].strip().split(': ')[1].split(' ')))
print(seeds)

lines = lines[2:]
arr=[[],[],[],[],[],[],[]]
ct=-1
for i in lines:
    if ":" in i:
        ct+=1
    elif i[0].isdigit():
        nums = list(map(int, i.strip().split(' ')))
        nums = (nums[1],nums[0],nums[2])
        arr[ct].append(nums)
for i in range(len(arr)):
    arr[i] = sorted(arr[i],key=lambda x: x[0])

minimum = float('inf')


for i in range(0,len(seeds),2):
    print("{} out of {}".format(i,len(seeds)))
    start=seeds[i]
    end = seeds[i]+seeds[i+1]
    n = seeds[i+1]
    seediter=int(sqrt(n))
    minseed=0
    minseedval =float('inf')
    ct=0
    for j in range(start,end,seediter):
        val = findloc(j,arr)
        if val<minseedval:
            minseed = ct
            minseedval = val
        ct+=1
    if minseed!=0:
        for j in range(start+(minseed-1)*seediter,start+(minseed+2)*seediter):
            minimum = min(minimum,findloc(j,arr))
print(minimum)
#20358599