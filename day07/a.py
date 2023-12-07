from functools import cmp_to_key
def comp(h1, h2):
    r1,arr1,_ = h1
    r2,arr2,_ = h2
    if(r1>r2):
        return -1
    elif (r1<r2):
        return 1
    else:
        for c in range(len(arr1)):
            if arr1[c] < arr2[c]:
                return -1
            elif arr1[c] > arr2[c]:
                return 1
    return 0
f = open("sample","r")
f= open("in","r")
lines = f.readlines()
rank_mapping = {'2': '2', '3': '3', '4': '4', '5': '5', '6': '6',
                    '7': '7', '8': '8', '9': '9', 'T': '10', 'J': '11',
                    'Q': '12', 'K': '13', 'A': '14'}
arr=[]
for i in lines:
    cards, bid = tuple(i.strip().split(" "))
    cards = list(cards)
    bid = int(bid)
    for j in range(len(cards)):
        cards[j] = int(rank_mapping[cards[j]])
    arr.append((cards,bid))
standings=[]
for i in arr:
    cards = i[0]
    s = set(cards)
    if len(s) == 1:
        standings.append((0,i[0],i[1]))
    elif len(s) == 2:
        ls = list(s)
        card1 = ls[0]
        card2 = ls[1]
        ct = cards.count(card1)
        if ct==4 or ct==1:
            standings.append((1,i[0],i[1]))
        else:
            standings.append((2,i[0], i[1]))
    else:
        maxMatches = 0
        ct = 0
        for j in s:
            if cards.count(j)>maxMatches:
                maxMatches = cards.count(j)
                ct = 0
            elif cards.count(j) == maxMatches:
                ct+=1
        if maxMatches == 3:
            standings.append((3, i[0], i[1]))
        elif maxMatches==2 and ct==1:
            standings.append((4,i[0], i[1]))
        elif maxMatches==2:
            standings.append((5,i[0], i[1]))
        else:
            standings.append((6,i[0],i[1]))
standings = sorted(standings, key=cmp_to_key(comp))
res=0     
for c,i in enumerate(standings):
    res+= (c+1)*i[2]
print(arr)
print(standings)
print(res)
#249483956