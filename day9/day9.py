def read_input():
    numbers = []
    with open('input.txt','r') as f:
        for line in f:
            numbers.append(int(line))
    return numbers

def find_sum(preamble, sum_needed):
    for number in preamble:
        if sum_needed - number in preamble:
            return sum_needed - number
    return None

def min_plus_max(numbers):
    numbers.sort()
    return numbers[0] + numbers[len(numbers)-1]

def process(numbers, preamble):
    preamble_set = set(numbers[:preamble])

    i = preamble
    while i < len(numbers):
        sum_needed = numbers[i]
        preamble_sum = find_sum(preamble_set, sum_needed)
        if preamble_sum is None:
            return sum_needed
        i += 1
        preamble_set = set(numbers[i-preamble:i])

def find_operands(numbers, error_number):
    i = 0
    num_tries = 1
    sum_numbers = 0
    while i < len(numbers):
        sum_numbers += numbers[i]
        if sum_numbers > error_number:
            i = num_tries
            num_tries += 1
            sum_numbers = 0
        elif sum_numbers == error_number:
            return numbers[num_tries-1:i+1]
        else:
            i += 1


preamble = 25
numbers = read_input()
error_number = process(numbers, preamble)
print(error_number)
operands = find_operands(numbers, error_number)
print(min_plus_max(operands))