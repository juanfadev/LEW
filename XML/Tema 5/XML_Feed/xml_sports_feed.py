import requests
import xmltodict
import xml.etree.ElementTree as ET



def main():
    response = requests.get('https://futbol.as.com/rss/futbol/segunda.xml')
    input_xml = response.content
    input_file = open('feed.xml', 'wb')
    input_file.write(input_xml)

    doc = xmltodict.parse(input_xml, encoding='utf-8', dict_constructor = dict)
    mydata = createNewXML(doc)
    myfile = open("segunda_division.xml", "wb")  
    myfile.write(mydata)  

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
        item.text = i['link']
        categories = ET.SubElement(item, 'categories')
        for c in i['category']:
            category = ET.SubElement(categories, 'category')
            category.text = i['category']

    # create a new XML file with the results
    mydata = ET.tostring(feed)  
    
    return mydata


    


if __name__ == '__main__':
  main()