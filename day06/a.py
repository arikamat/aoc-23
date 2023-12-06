f = open("sample","r")
f= open("in","r")
lines = f.readlines()
time = list(map(int,lines[0].strip().split(':')[1].strip().split()))
distance = list(map(int,lines[1].strip().split(':')[1].strip().split()))
ans=1
for i in range(len(time)):
    ct=0
    for j in range(time[i]):
        if j*(time[i]-j) > distance[i]:
            ct+=1
    ans*=ct
print(ans)
#2374848