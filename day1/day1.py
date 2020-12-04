def build_list():
    entries = []
    with open('input.txt','r') as f:
        for line in f:
            entries.append(line[:-1])
    return entries

def rec_operands(numOperands, list, target):
    for i in range(len(list)):
        result = target - int(list[i])

        if result == 0 and numOperands == 1:
            #we are done, return and multiply
            return int(list[i])
        elif numOperands > 1 and result > 0:
            #we have more operands to find
            op = rec_operands(numOperands - 1, list[i:len(list)], result)
            if op is not None and op != 0:
                total = op * int(list[i])
                return total

print("Two")
print(rec_operands(2, build_list(), 2020))
print(rec_operands(3, build_list(), 2020))