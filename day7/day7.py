class Bag:
    color : str
    contents : dict

    def __init__(self, data):
        self.contents = dict()
        bags = data.split('contain')
        self.color = bags[0].replace('bags','').strip()
        if bags[1].strip() != 'no other bags.':
            for bag in bags[1].split(','):
                bag = bag.strip().split(' ')
                count = bag[0]
                color = bag[1] + ' ' + bag[2]
                self.contents[color] = count

    def __str__(self):
        contains = 'contains '
        i = 0
        for k,v in self.contents.items():
            if i != 0:
                contains += ', '
            contains += v + ' ' + k
            i += 1
        return self.color + ' ' + contains
    
    def contains(self, bag):
        return self.contents.get(bag) is not None

def count_bags(curbag, bags):
    sum_bags = 1
    contents = curbag.contents
    for color in contents:
        count = contents.get(color)
        if count is not None:
            sum_bags += int(count) * count_bags(bags.get(color), bags)
    return sum_bags
        
def load_bags():
    bags = dict()
    contents = []
    with open('input.txt','r') as f:
        contents = f.read().split('\n')

    for line in contents:
        bag = Bag(line.strip())
        bags[bag.color] = bag
    return bags

bags = load_bags()
can_contain_gold = []

for bag in bags.values():
    print(bag)
    if bag.contains('shiny gold'):
        can_contain_gold.append(bag.color)
other_bags = 0
for contains_gold in can_contain_gold:
    for bag in bags.values():
        if bag.contains(contains_gold) and bag.color not in can_contain_gold:
            can_contain_gold.append(bag.color)

shiny_gold = bags.get('shiny gold')
print('shiny gold contains:',count_bags(shiny_gold, bags) -1)

print('can contain gold:',len(can_contain_gold))