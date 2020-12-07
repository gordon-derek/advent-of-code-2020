def read_input():
    tickets = []
    with open('input.txt','r') as f:
        for line in f:
            tickets.append(line.strip())
    return tickets

def half(start, end):
    return int((start + end) / 2)

def calc_id(row, col):
    return row * 8 + col

def solve(input):
    rows = input[:-3]
    cols = input[-3:]
    front = 0
    back = 127
    cur_seat = half(front,back)
    for row in rows:
        if row == 'F':
            back = cur_seat
        elif row == 'B':
            front = cur_seat + 1
        cur_seat = half(front,back)
    row = cur_seat
    front = 0
    back = 7
    cur_seat = half(front,back)
    for col in cols:
        if col == 'R':
            front = cur_seat + 1
        elif col == 'L':
            back = cur_seat
        cur_seat = half(front,back)
    col = cur_seat
    return [row,col]

tickets = read_input()
ids = {}
seats = [['O']*8 for i in range(128)]
highest_id = 0

for ticket in tickets:
    result = solve(ticket)
    seat_id = calc_id(result[0],result[1])
    if seat_id > highest_id:
        highest_id = seat_id
    print('ticket',ticket,'row',result[0],'col',result[1],'seat ID', calc_id(result[0], result[1]))
    seats[result[0]][result[1]] = 'X'
    ids[seat_id] = True

#calculate your missing seat
for row in range(len(seats)):
    for col in range(len(seats[row])):
        if seats[row][col] == 'O':
            seat_id = calc_id(row,col)
            if ids.get(int(seat_id)-1) is not None\
                and ids.get(int(seat_id)+1) is not None:
                print('your seat is', seat_id, 'row', row, 'col', col)

print('Highest Seat ID:',highest_id)
