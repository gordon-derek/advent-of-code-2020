class Command:
    command : str
    increment : int

    def __init__(self, command, increment):
        self.command = command
        self.increment = int(increment)
    
    def __str__(self):
        return self.command + ' ' + str(self.increment)

def read_input():
    commands = []
    with open('input.txt','r') as f:
        for line in f:
            line = line.strip().split(' ')
            commands.append(Command(line[0], line[1]))
    return commands

def process(commands):
    acc = 0
    indexes_used = set()
    i = 0
    while i < len(commands):
        command = commands[i]
        indexes_used.add(i)
        if command.command == 'nop':
            i += 1
        elif command.command == 'acc':
            acc += command.increment
            i += 1
        elif command.command == 'jmp':
            i += command.increment
        if i in indexes_used:
            return str(acc)
    return 'success ' + str(acc)

def repair(commands):
    for command in commands:
        if command.command == 'nop':
            command.command = 'jmp'
            output = process(commands)
            if 'success' in output:
                return output
            else:
                command.command = 'nop'
        elif command.command == 'jmp':
            command.command = 'nop'
            output = process(commands)
            if 'success' in output:
                return output
            else:
                command.command = 'jmp'

commands = read_input()
print(process(commands))
print(repair(commands))