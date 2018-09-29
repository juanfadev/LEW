import requests
import xmltodict
from lxml import etree as ET
import sys



def main():
    response = requests.get('https://futbol.as.com/rss/futbol/segunda.xml')
    input_xml = response.content
    input_file = open('feed.xml', 'wb')
    input_file.write(input_xml)

    with open('feed.xml', encoding='utf-8') as fd:
        doc = xmltodict.parse(fd.read(), encoding='utf-8', dict_constructor = dict)

        createNewXML(doc)
    

def createNewXML(input_xml):
    # create the file structure
    root = input_xml['rss']['channel']
    feed = ET.Element('feed')
    feed.set('title', root['title'])
    feed.set('link', root['link'])
    feed.set('published', root['pubDate'])
    feed.set('lang', root['language'])
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

    print (ET.tostring(feed, encoding="utf-8"))
    # create a new XML file with the results
    ET.ElementTree(feed).write('segunda_division.xml',encoding="UTF-8",xml_declaration=True) 
    


    


if __name__ == '__main__':
  main()