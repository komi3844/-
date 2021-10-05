import lxml.etree as ET


with open('9018789b-3438-4933-a1ae-caab18bfd3aa (1).xml', encoding="utf8") as f:
    tree = ET.parse(f)
    root = tree.getroot()

    for elem in root.getiterator():
        try:
            elem.text = elem.text.replace('&#13;', 'xxix')
        except AttributeError:
            pass


tree.write('output.xml', xml_declaration=True, method='xml', encoding="utf8")
