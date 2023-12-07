from functools import cmp_to_key
import itertools
def comp(h1, h2):
    r1,arr1,_ = h1
    r2,arr2,_ = h2
    # print("here1")
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
def getRate(cards):
    # print(cards)
    s = set(cards)
    if len(s) == 1:
        return 0
    elif len(s) == 2:
        ls = list(s)
        card1 = ls[0]
        card2 = ls[1]
        ct = cards.count(card1)
        if ct==4 or ct==1:
            return 1
        else:
            return 2
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
            return 3
        elif maxMatches==2 and ct==1:
            return 4
        elif maxMatches==2:
            return 5
        else:
            return 6
f = open("sample","r")
f= open("in","r")
lines = f.readlines()
rank_mapping = {'2': '2', '3': '3', '4': '4', '5': '5', '6': '6',
                    '7': '7', '8': '8', '9': '9', 'T': '10', 'J': '0',
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
bank = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

for c,i in enumerate(arr):
    cards = i[0]
    bid = i[1]
    # print(cards,bid)
    oldcards = i[0].copy()
    if 0 in cards:
        possible=[]
        ct = cards.count(0)
        for _ in range(ct):
            cards.remove(0)
        a=list(itertools.combinations_with_replacement(bank, ct))
        # print(a)
        for j in a:
            tempcards = cards + list(j)
            possible.append((getRate(tempcards),oldcards,bid))
        possible = sorted(possible,key=cmp_to_key(comp))
        standings.append(possible[-1])
    else:
        rank = getRate(cards)
        standings.append((rank,cards,bid))




for i in arr:
    cards = i[0]
    bid =  i[1]
    
    
    
standings = sorted(standings, key=cmp_to_key(comp))
res=0     
for c,i in enumerate(standings):
    res+= (c+1)*i[2]
# print(arr)
print(standings)
print(res)
#252137472