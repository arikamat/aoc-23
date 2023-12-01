def extract_digits(input_string):
    return ''.join(char for char in input_string if char.isdigit())

f = open("in","r")
lines = f.readlines()
s=0
for i in lines:
    a = extract_digits(i)
    if len(a)>=2:
        a = a[0]+a[-1]
        a = int(a)
        s+=a
    elif len(a)==1:
        a = a+a
        a = int(a)
        s+=a

print(s)
