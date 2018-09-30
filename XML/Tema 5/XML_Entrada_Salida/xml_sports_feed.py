import requests
import xmltodict
from lxml import etree as ET
import sys
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm, inch
import datetime

sample_style_sheet = getSampleStyleSheet()

PAGESIZE = (140 * mm, 216 * mm)
BASE_MARGIN = 5 * mm


def main():
    response = requests.get('https://futbol.as.com/rss/futbol/segunda.xml')
    input_xml = response.content
    input_file = open('feed.xml', 'wb')
    input_file.write(input_xml)

    with open('feed.xml', encoding='utf-8') as fd:
        doc = xmltodict.parse(fd.read(), encoding='utf-8', dict_constructor = dict)

        my_doc = SimpleDocTemplate(
            'resumenSegundaDivision'+datetime.datetime.now().strftime('%Y-%m-%d-%H_%M_%S') + '.pdf',
            pagesize=PAGESIZE,
            topMargin=BASE_MARGIN,
            leftMargin=BASE_MARGIN,
            rightMargin=BASE_MARGIN,
            bottomMargin=BASE_MARGIN
        )
        paragraphs = []
        
        createNewXML(doc, paragraphs)

        my_doc.build(paragraphs)
    

def createNewXML(input_xml, paragraphs):
    paragraphs.extend([Paragraph("Segunda División", sample_style_sheet['Heading1'])])
    # create the file structure
    root = input_xml['rss']['channel']
    feed = ET.Element('feed')
    feed.set('title', root['title'])
    feed.set('link', root['link'])
    feed.set('published', root['pubDate'])
    feed.set('lang', root['language'])
    paragraphs.extend([Paragraph(root['title'], sample_style_sheet['Heading2'])])
    copyright = ET.SubElement(feed, 'copyright')
    copyright.text = root['copyright']
    image = ET.SubElement(feed,'image')
    image.set('title', root['image']['title'])
    imURL = ET.SubElement(image, 'url')
    imURL.text = root['image']['url']
    imLink = ET.SubElement(image, 'link')
    imLink.text = root['image']['link']
    items = ET.SubElement(feed, 'items')
    for i in root['item']:
        item = ET.SubElement(items, 'item')
        item.set('title', i['title'])
        item.set('description', i['description'])
        item.set('creator', i['dc:creator'])
        link =  ET.SubElement(item, 'link')
        link.text = i['link']
        item.text = ET.CDATA(i['content:encoded'])
        categories = ET.SubElement(item, 'categories')
        for c in i['category']:
            category = ET.SubElement(categories, 'category')
            category.text = c
        paragraphs.extend([Paragraph(i['title'], sample_style_sheet['Heading3'])])
        paragraphs.extend([Paragraph(i['description'], sample_style_sheet['BodyText'])])
        
    # create a new XML file with the results
    ET.ElementTree(feed).write('segunda_division.xml',encoding="UTF-8",xml_declaration=True, pretty_print=True) 
    
if __name__ == '__main__':
  main()