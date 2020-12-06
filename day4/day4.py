import re

class Passport:
    fields = {}
    keys = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
    def __init__(self, data):
        self.fields = {key: None for key in self.keys}
        self.populate_from_data(data)

    def __str__(self):
        return '{byr},{iyr},{eyr},{hgt},{hcl},{ecl},{pid}'.format(byr=self.fields['byr'], iyr=self.fields['iyr'], eyr=self.fields['eyr'], hgt=self.fields['hgt'], hcl=self.fields['hcl'], ecl=self.fields['ecl'], pid=self.fields['pid'])
    
    def populate_from_data(self, data):
        for line in data.split('\n'):
            for entry in line.split(' '):
                field = entry.split(':')
                self.fields[field[0]] = field[1]

    def validate(self):
        valid = True
        for k,v in self.fields.items():
            if v is None and k != 'cid':
                return False
            elif k == 'byr' and not 1920 <= int(v) <= 2002:
                return False
            elif k == 'iyr' and not 2010 <= int(v) <= 2020:
                return False
            elif k == 'eyr' and not 2020 <= int(v) <= 2030:
                return False
            elif k == 'hgt':
                if v[-2:] == 'cm':
                    if int(v[:-2]) > 193 or int(v[:-2]) < 150:
                        return False
                elif v[-2:] == 'in': 
                    if int(v[:-2]) > 76 or int(v[:-2]) < 59:
                        return False
                else:
                    return False
            elif k == 'hcl':
                if len(v) == 7:
                    pattern = re.compile('^[a-f0-9]{6}$')
                    if not pattern.match(v[1:]):
                        return False
                else:
                    return False
            elif k == 'ecl' and v not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                valid = False
            elif k == 'pid':
                if len(v) != 9:
                    return False

        return valid


def get_input():
    passports = []
    contents = ''
    with open('input.txt','r') as f:
        contents = f.read().split('\n\n')
        
    for data in contents:
        passports.append(Passport(data))

    return passports

passports = get_input()
num_valid = 0
for passport in passports:
    if passport.validate():
        print(passport)
        num_valid += 1

print(num_valid)