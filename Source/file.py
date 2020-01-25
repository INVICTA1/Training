import io, re
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage


def extract_txt_from_pdf(pdf_path):
    resource_manager = PDFResourceManager()  # используется для хранения общих ресурсов, таких как шрифты или изображения.(Создаем экземпляр ресурса менеджера)
    take_file_handle = io.StringIO()  # создаем файловый объект
    converter = TextConverter(resource_manager, take_file_handle)  # (создание конвертера)
    page_interpreter = PDFPageInterpreter(resource_manager,
                                          converter)  # создаем объект интерпритаторов который извлечет текст
    with open(pdf_path, 'rb') as file:
        for page in PDFPage.get_pages(file, caching=True, check_extractable=True):
            page_interpreter.process_page(page)
        text = take_file_handle.getvalue()
    converter.close()
    take_file_handle.close()

    if text:
        return text


if __name__ == '__main__':
    with  io.open('result.txt', 'w+', encoding="utf-8") as txt_file:
        text = extract_txt_from_pdf(r'..\Books\fw9.pdf')

        sentences = re.split('[.!?]\s',text )
        for sentence in sentences:
            txt_file.write(str(sentence) + '.\n')