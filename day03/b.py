f = open("sample","r")
f= open("in","r")
lines = f.readlines()

def get_border_coordinates(matrix, target_row, column_start, column_end):
    rows, cols = len(matrix), len(matrix[0])
    border_coordinates = []

    for r in range(target_row-1, target_row+2):
        for c in range(column_start-1, column_end+2):
            if r<0 or c<0 or r>=rows or c>=cols:
                continue
            else:
                border_coordinates.append((r,c))
    return border_coordinates
    

grid=[]
d={} # coord of * : num
for i in lines:
    grid.append(list(i.strip()))


for row,i in enumerate(grid):
    j=0
    while j<len(i):
        if i[j].isdigit():
            start = j
            while j<len(i) and i[j].isdigit():
                j+=1
            end = j
            coords = get_border_coordinates(grid,row, start, end-1)
            for r,c in coords:
                if grid[r][c]=='*':
                    tup = (r,c)
                    num=int(''.join(i[start:end]))
                    if tup not in d:
                        d[tup]=[]
                    d[tup].append(num)
                    break
        j+=1
s =0
for i in d:
    if len(d[i])==2:
        s+=(d[i][0]*d[i][1])
print(s)