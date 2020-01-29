import re
import xml.etree.ElementTree as ET
path_file_xml = '..\Recourse\Input\XML.xml'


class XML_tags():
    def __init__(self, name, tags, text):
        self.name = name
        self.tags = tags
        self.text = text

    def output_value(self):

        for i in range(len(self.tags)):
            print('\n'+self.name[i]+'\n')
            for j in range(len(self.tags[i])):
                if self.tags[i][j]=='':
                    print("don't have tags")
                else:
                    print(self.tags[i][j] + ':', self.text[i][j])


def parse_XML(path_xml):
    tree = ET.parse(path_xml)
    root = tree.getroot()
    print(tree)
    name = []
    tag_name = []
    tag_text = []
    for child in root:
        name.append(child.tag)
        text = []
        tags = []
        for tag in child:
            tags.append(tag.tag)
            text.append(tag.text)
        tag_name.append(tags)
        tag_text.append(text)
    return name, tag_name, tag_text


name = parse_XML(path_file_xml)
file1 = XML_tags(name[0], name[1], name[2])
print(file1.output_value())
