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
for i in range(len(arr)):
    arr[i] = sorted(arr[i],key=lambda x: x[0])

minimum = float('inf')
for i in seeds:
    minimum=min(minimum,findloc(i,arr))
print(minimum)
#31599214