import io
from os import path
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage


def parse_pdf(pdf_path):
    resource_manager = PDFResourceManager()  # используется для хранения общих ресурсов, таких как шрифты или изображения.(Создаем экземпляр ресурса менеджера)
    input_stream = io.StringIO()  # создаем файловый объект
    converter = TextConverter(resource_manager, input_stream)  # (создание конвертера)
    page_interpreter = PDFPageInterpreter(resource_manager,
                                          converter)  # создаем объект интерпритаторов который извлечет текст
    with open(pdf_path, 'rb') as file:
        for page in PDFPage.get_pages(file, caching=True, check_extractable=True):
            page_interpreter.process_page(page)
        text = input_stream.getvalue()
    converter.close()
    input_stream.close()

    if text:
        return text


def get_output_path(resource_path):
    full_name = path.basename(resource_path)
    name = path.splitext(full_name)[0]
    way = "..\Recourse\Output\\" + name + ".txt"
    return way

if __name__=='__main__':
    pass