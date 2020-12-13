def read_input():
    adapters = []
    with open('input.txt','r') as f:
        for line in f:
            adapters.append(int(line))
    return adapters

def calculate(adapters):
    current_jolt = 0
    one_jolt_diff = []
    three_jolt_diff = []
    adapters.sort()
    for adapter in adapters:
        if adapter - current_jolt == 1:
            one_jolt_diff.append(adapter)
        elif adapter - current_jolt == 3:
            three_jolt_diff.append(adapter)
        current_jolt = adapter
    #device adapter is 3 jolts
    three_jolt_diff.append(current_jolt + 3)
    return one_jolt_diff, three_jolt_diff

def get_arrangements(adapters):
    arrangements = {0:1}
    for adapter in adapters:
        arrangements[adapter] = 0

        if adapter - 1 in arrangements:
            arrangements[adapter] += arrangements[adapter-1]
        if adapter - 2 in arrangements:
            arrangements[adapter] += arrangements[adapter-2]
        if adapter - 3 in arrangements:
            arrangements[adapter] += arrangements[adapter-3]
    return arrangements[max(arrangements)]


adapters = read_input()
one_vs_three_jolt = calculate(adapters)
print(len(one_vs_three_jolt[0]), 'One Jolt Differences and', len(one_vs_three_jolt[1]), 'Three Jolt Differences.')
print(len(one_vs_three_jolt[0]) * len(one_vs_three_jolt[1]))
print(get_arrangements(adapters))