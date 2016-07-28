from lxml import etree
page = etree.Element('xml')
doc = etree.ElementTree(page)

a = page.append(etree.Element("fixityEvent"))
new_element = etree.Element('blaaaaa')
page.insert(0,new_element)

premiso = etree.Element('premis')

new_element.insert(0, premiso) 
premiso.text = 'TESTSTSTSTSTST'
outFile = open('premis.xml','w')
doc.write(outFile)
