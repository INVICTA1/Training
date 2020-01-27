import io, re
from Source.pdfProcesser import output_path, extract_txt_from_pdf


def splitting_text_into_sentences():
    pdf_path = r'..\Recourse\Input\fw9.pdf'
    regex = ('[.!?]\s')
    with  io.open(output_path(pdf_path), 'w+', encoding="utf-8") as txt_file:
        text = extract_txt_from_pdf(pdf_path)
        sentences = re.split(regex, text)
        for sentence in sentences:
            txt_file.write(str(sentence) + '.\n')


def word_after_U_S():
    pdf_path = r'..\Recourse\Input\fw9.pdf'
    text = extract_txt_from_pdf(pdf_path)
    regex_US = '(\s\w\.\w\.\s)(\w+)'
    word = re.findall(regex_US, text)
    for i in word:
        print(i[1])

word_after_U_S()