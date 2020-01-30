from Source.xmlProcesser import *
from Source.Fw9Parser import *
from Source.tasks import task2_find_emails
from os import path


def parsing_file(path_file):
    fun = {'.pdf': splitting_text_into_sentences, '.xml': output_xml_data, '.txt': task2_find_emails}
    full_name = path.basename(path_file)
    expansion = path.splitext(full_name)[1]
    for key, value in fun.items():
        if key == expansion:
            value(path_file)
            print('aasd')


path_files = '../Recourse/Input/..'
parsing_file(path_files)
