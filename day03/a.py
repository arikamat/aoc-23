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
res=[]
for i in lines:
    grid.append(list(i.strip()))


for c1,i in enumerate(grid):
    j=0
    while j<len(i):
        if i[j].isdigit():
            start = j
            while j<len(i) and i[j].isdigit():
                j+=1
            end = j
            coords = get_border_coordinates(grid,c1, start, end-1)
            for r,c in coords:
                if grid[r][c]!='.' and not grid[r][c].isdigit():
                    res.append(int(''.join(i[start:end])))
                    break
        j+=1
print(sum(res))