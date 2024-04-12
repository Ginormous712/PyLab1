from datetime import datetime

from lxml import etree
from Airport.Airport import Airport
from Airport.UI import UI


def validate(xml_path: str, xsd_path: str) -> bool:

    xmlschema_doc = etree.parse(xsd_path)
    xmlschema = etree.XMLSchema(xmlschema_doc)

    xml_doc = etree.parse(xml_path)
    result = xmlschema.validate(xml_doc)

    return result


if __name__ == '__main__':
    xml_path = 'Resources/airport.xml'
    xsd_path = 'Resources/Airport.xsd'
    if validate(xml_path, xsd_path):
        print('XML validated')
    else:
        print('XML not validated')

    ui = UI(xml_path)
    ui.menu()




