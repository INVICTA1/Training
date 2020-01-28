import re
import xml.etree.ElementTree as ET
regex='\w{3}'
tree = ET.parse('..\Recourse\Input\XML.xml')
root = tree.getroot()
print(root.attrib)
for child in root:
    print(child.tag,child.attrib)
    for child2 in child:
        print(child2.tag)
