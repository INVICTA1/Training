import re, io
from Source.pdfProcesser import output_path, extract_txt_from_pdf


# создать класс user


class User():
    def __init__(self, email, mobile_phone, name):
        self.email = email
        self.mobile_phone = mobile_phone
        self.name = name

    def userInformation(self):
        return self.name, self.mobile_phone, self.email


def findUser():
    pdf_path = r'..\Recourse\Input\resume.pdf'
    with io.open(output_path(pdf_path), 'w+', encoding="utf-8") as file:
        text = extract_txt_from_pdf(pdf_path)
        regex_name = (r'\w+\s\w+\s\w+')
        regex_email = (r'\w+\.\w+@\w+.com')
        regex_mobile_phone = (r'[+]\d{12}')
        email = re.findall(regex_email, text)[0]
        mobile_phone = re.findall(regex_mobile_phone, text)[0]
        name = re.findall(regex_name, text)[0]
        return email, mobile_phone, name


data = findUser()
maksim = User(data[0], data[1], data[2])
print(maksim.userInformation())
