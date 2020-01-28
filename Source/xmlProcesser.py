import re
import xml.etree.ElementTree as ET
regex='\w{3}'
tree = ET.parse('..\Recourse\Input\XML.xml')
root = tree.getroot()
print(root.attrib)
print(root)
