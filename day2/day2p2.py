class Password:
    position1 = 0
    position2 = 0
    reqLetter = ''
    password = ''

    def __init__(self, position1, position2, reqLetter, password):
        self.position1 = int(position1)-1
        self.position2 = int(position2)-1
        self.reqLetter = reqLetter
        self.password = password

    def validate_password(self):
        return True if (self.password[self.position1] == self.reqLetter or self.password[self.position2] == self.reqLetter)\
             and not (self.password[self.position1] == self.reqLetter and self.password[self.position2] == self.reqLetter) else False

def solve_for_input():
    valid_count = 0
    with open('input.txt','r') as f:
        for line in f:
            dash = line.index('-')
            space1 = line.index(' ')
            colon = line.index(':')
            if Password(line[0:dash], line[dash+1:space1], line[space1+1], line[colon+2:]).validate_password():
                valid_count += 1
    return valid_count

print(solve_for_input())