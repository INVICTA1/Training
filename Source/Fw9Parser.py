import io, re
from Source.pdfProcesser import get_output_path, parse_pdf


def splitting_text_into_sentences(pdf_path):
    regex = ('[.!?]\s')
    with  io.open(get_output_path(pdf_path), 'w+', encoding="utf-8") as txt_file:
        text = parse_pdf(pdf_path)
        sentences = re.split(regex, text)
        for sentence in sentences:
            txt_file.write(str(sentence) + '.\n')


def word_after_U_S():
    pdf_path = r'..\Recourse\Input\fw9.pdf'
    text = parse_pdf(pdf_path)
    regex_US = '(\s\w\.\w\.\s)(\w+)'
    word = re.findall(regex_US, text)
    for i in word:
        print(i[1])
if __name__=='__main__':
    word_after_U_S()
    pdf_path = r'..\Recourse\Input\fw9.pdf'
    splitting_text_into_sentences(pdf_path)