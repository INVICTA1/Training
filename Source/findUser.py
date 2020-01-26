import re, io
from Source.processingPDF import output_path, extract_txt_from_pdf


def findUser():
    pdf_path = r'..\Recourse\Input\resume.pdf'
    user = {'name': '', 'email': '', 'mobile_phone': ''}
    address = []
    regex_name = (r'\w+\s\w+\s\w+')
    regex_email = (r'\w+\.\w+@\w+.com')
    regex_mobile_phone = (r'[+]\d{12}')
    with io.open(output_path(pdf_path), 'w+', encoding="utf-8") as file:
        text = extract_txt_from_pdf(pdf_path)
        user['email'] = re.findall(regex_email, text)[0]
        user['mobile_phone'] = re.findall(regex_mobile_phone, text)[0]
        user['name'] = re.findall(regex_name, text)[0]
        for key, value in user.items():
            file.write(key +':'+value+'\n')


if __name__ == '__main__':
    findUser()
