import re
import pdb
def replace_first_letter_with_number(line):
    word_to_number = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    idxsub = {}
    for i in word_to_number:    
        for match in re.finditer(i, line):
            idx = match.start()
            idxsub[idx] = word_to_number[i]
    keys = list(idxsub.keys())
    keys.sort()
    linesplit = list(line)
    for i in keys:
        linesplit[i] = idxsub[i]
    return ''.join(linesplit)
def extract_digits(input_string):
    return ''.join(char for char in input_string if char.isdigit())

# original_string = "onethreefiveeightthree"
# pdb.set_trace()
# result = replace_first_letter_with_number(original_string)
# print(result)


f = open("in","r")
lines = f.readlines()
s=0
for i in lines:
    i = replace_first_letter_with_number(i)
    print(i)
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
