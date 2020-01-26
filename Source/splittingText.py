import io,re
from .processingPDF import output_path,extract_txt_from_pdf
def splitting_text_into_sentences():
    pdf_path = r'..\Recourse\Input\fw9.pdf'
    regex = ('[.!?]\s[A-B]')
    with  io.open(output_path(pdf_path), 'w+', encoding="utf-8") as txt_file:
        text = extract_txt_from_pdf(pdf_path)
        sentences = re.split(regex, text)
        for sentence in sentences:
            txt_file.write(str(sentence) + '.\n')

