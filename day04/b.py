f = open("sample","r")
f= open("in","r")
lines = f.readlines()

copies=[1]*len(lines)
for c,i in enumerate(lines):
    i = i.strip()
    i = i.split(': ')[1]
    arr = i.split(' | ')
    winningnums = arr[0].strip().split(' ')

    cardnums = arr[1].strip().split(' ')
    ct=0
    for j in cardnums:
        if j.isdigit() and j in winningnums:
            ct+=1
    for j in range(c+1,c+ct+1):
        copies[j] += copies[c]
# print(copies)
print(sum(copies))
#6857330