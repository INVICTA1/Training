import re


def task1():
    numbers = []
    regex_private = r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}'
    regex_taxi = r'[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}'
    while True:
        number = input()
        if number == '':
            break
        else:
            numbers.append(number)
    for num in numbers:
        if re.fullmatch(regex_private, num) != None:
            print(num, ':Private')
        elif re.fullmatch(regex_taxi, num) != None:
            print(num, ':Taxi')
        else:
            print(num, ':Fail')


def task2():
    path_txt = '../Recourse/Input/tasks.txt'
    with open(path_txt, 'r') as file:
        text=file.read()
        regex = '[\w*\'_-]+@[\w\d.\'_-]+'
        emails = re.findall(regex, text, flags=re.ASCII)
        print()
task2()