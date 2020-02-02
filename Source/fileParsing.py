from Source.xmlProcesser import *
from Source.Fw9Parser import *
from Source.tasks import output_emails_in_file
from os import path, listdir


def parsing_directory(path_files):
    files = listdir(path_files)
    fun = {'.pdf': splitting_text_into_sentences, '.xml': output_data_in_file, '.txt': output_emails_in_file}
    for file in files:
        expansion = path.splitext(file)[1]
        path_file=path.join(path_files,file)
        for key, value in fun.items():
                if key == expansion:
                    value(path_file)


if __name__ == '__main__':
    path_files = '../Recourse/Input/'
    parsing_directory(path_files)
