def get_input():
    answers = []
    contents = ''
    with open('input.txt','r') as f:
        contents = f.read().split('\n\n')
        
    for data in contents:
        answers.append(data.replace('\n',' '))

    return answers
    
def sum_answers(answers):
    sum_answers_unique = 0
    sum_answers_same = 0
    for answer in answers:
        set_answers = set()
        for char in answer:
            if char != ' ':
                set_answers.add(char)
        sum_answers_unique += len(set_answers)
        for person in answer.split(' '):
            person_answers = set()
            for char in person:
                person_answers.add(char)
            set_answers = set_answers & person_answers
        sum_answers_same += len(set_answers)
    return [sum_answers_unique, sum_answers_same]

answers = get_input()
sum_answers = sum_answers(answers)
print(sum_answers[0], sum_answers[1])