f = open("sample","r")
f= open("in","r")
lines = f.readlines()
ans=0
for i in lines:
    i = i.strip()
    i = i.split(': ')[1]
    arr = i.split(' | ')
    winningnums = arr[0].strip().split(' ')

    cardnums = arr[1].strip().split(' ')
    score=0
    for j in cardnums:
        if j.isdigit() and j in winningnums:
            if score==0:
                score=1
            else:
                score*=2
    ans+=score
print(ans)
#27454