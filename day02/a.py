def extract_digits(input_string):
    return int(''.join(char for char in input_string if char.isdigit()))
f = open("sample","r")
f= open("in","r")
lines = f.readlines()

res=[]

for c,i in enumerate(lines):
    a = i.split(':')
    sets = a[1].split(';')
    d = {'r': 0, 'g': 0, 'b': 0}
    for j in sets:
        colors = j.split(', ')
        for k in colors:
            num = extract_digits(k)
            if 'blue' in k:
                d['b'] = max(d['b'], num)
            if 'red' in k:
                d['r'] = max(d['r'], num)
            if 'green' in k:
                d['g'] = max(d['g'], num)
    if d['r']<=12 and d['g']<=13 and d['b']<=14:
        res.append(c+1)
print(sum(res))

#2061