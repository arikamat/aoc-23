f = open("sample","r")
f= open("in","r")
lines = f.readlines()
t = int(lines[0].replace(' ','').strip().split(':')[1].strip())
d = int(lines[1].replace(' ','').strip().split(':')[1].strip())

lptr = 0
rptr = t
res=[]
while True:
    far = lptr*(t-lptr)
    if far > d:
        break
    lptr+=1

while True:
    far = rptr*(t-rptr)
    if far > d:
        break
    rptr-=1 

print(rptr-lptr+1)

#39132886