def read_input():
    seats = []
    with open('input.txt','r') as f:
        for line in f:
            row = []
            for char in line.strip():
                row.append(char)
            seats.append(row)

        return seats

def num_occupied(seats):
    num_occupied = 0
    for row in seats:
        for seat in row:
            if seat == '#':
                num_occupied += 1
    return num_occupied

def perform_flips(rows, flips):
    for flip in flips:
        i = int(flip[0])
        j = int(flip[1])
        if rows[i][j] == '#':
            rows[i][j] = 'L'
        else:
            rows[i][j] = '#'
    return rows

def count_occupied(rows):
    occupied = 0
    for row in rows:
        for seat in row:
            if seat == '#':
                occupied += 1
    return occupied

def solve(rows):
    changed = True
    x = 0
    while changed is True:
        flips = []
        x+=1
        changed = False
        for i in range(len(rows)):
            for j in range(len(rows[i])):
                seat = rows[i][j]
                lower_row = i-1
                upper_row = i+1
                lower_col = j-1
                upper_col = j+1
                if i == 0:
                    lower_row = i
                elif i == len(rows)-1:
                    upper_row = i
                if j == 0:
                    lower_col = j
                elif j == len(rows[i])-1:
                    upper_col = j
                sliced_seats = [rows[k][lower_col:upper_col+1] for k in range(lower_row,upper_row+1)]
                if seat == 'L':
                    if num_occupied(sliced_seats) == 0:
                        flips.append([i,j])
                elif seat == '#':
                    if num_occupied(sliced_seats) > 4:
                        flips.append([i,j])
        if len(flips) != 0:
            rows = perform_flips(rows, flips)
            changed = True
    print('iterated:', x, 'times')
    return rows

rows = read_input()
solved = solve(rows)
print('occupied:', count_occupied(solved))