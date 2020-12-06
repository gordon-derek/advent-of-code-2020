def solve_for_input(right, down):
    num_down = down
    rightward_index = 0
    num_trees = 0
    with open('input.txt','r') as f:
        for line in f:
            if num_down == 0:
                rightward_index += right
                if line[rightward_index % 31] == '#':
                    num_trees += 1
                num_down = down
            num_down -= 1
        return num_trees

print(solve_for_input(1,1)
    * solve_for_input(3,1)
    * solve_for_input(5,1)
    * solve_for_input(7,1)
    * solve_for_input(1,2))