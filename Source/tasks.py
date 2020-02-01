import re
from os import path

def task1_true_numbers():
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


def task2_find_emails(path_txt):

    emails = []
    regex_email = "[\d\w\'\._-]+[^\s.;'@,\-]@[^\s.;'@,\-][\d\w\'\._-]+"
    regex_check_last_symbol = '[^\s.+-][\w*\'\._-]+[^\s.+-]@[^\s.+-][\w\d\.\'_-]+[^.+\s-]'
    regex_check_on_point = '[\w*\'\._-]*(\.\.)[\w*\'\._-]*@[\w*\'\._-]*|[\w*\'\._-]*@[\w*\'\._-]*(\.\.)[\w*\'\._-]*'
    with open(path_txt, 'r', encoding="utf_8_sig") as file:
        text = file.read()

    all_emails = re.findall(regex_email, text, flags=re.ASCII)
    for i in re.finditer(regex_check_last_symbol, ' '.join(all_emails)):
        emails.append(i[0])
    for i in re.finditer(regex_check_on_point, ' '.join(emails)):
        emails.remove(i[0])
    return emails

def output_emails_in_file(path_txt):
    emails=task2_find_emails(path_txt)
    full_name = path.basename(path_txt)
    name = path.splitext(full_name)[0]
    way = "..\Recourse\Output\\" + name + ".txt"
    with open(way,'w') as file_emails:
        for i in emails:
            file_emails.write(i+', ')


if __name__=='__main__':
    path_txt = '../Recourse/Input/tasks.txt'
    output_emails_in_file(path_txt)
