class Password:
    minimum = 0
    maximum = 0
    reqLetter = ''
    password = ''

    def __init__(self, minimum, maximum, reqLetter, password):
        self.minimum = int(minimum)
        self.maximum = int(maximum)
        self.reqLetter = reqLetter
        self.password = password

    def validate(self):
        numLetter = self.password.count(self.reqLetter)
        return self.minimum <= numLetter <= self.maximum

def solve_for_input():
    valid_count = 0
    with open('input.txt','r') as f:
        for line in f:
            dash = line.index('-')
            space1 = line.index(' ')
            colon = line.index(':')
            if Password(line[0:dash], line[dash+1:space1], line[space1+1], line[colon+2:]).validate():
                valid_count += 1
    return valid_count

print(solve_for_input())