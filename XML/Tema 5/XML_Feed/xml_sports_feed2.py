import requests
import xmltodict
import xml.etree.ElementTree as ET



def main():
    response = requests.get('https://futbol.as.com/rss/futbol/segunda.xml')
    input_xml = response.content
    input_file = open('feed.xml', 'wb')
    input_file.write(input_xml)

    createNewXML(ET.parse('feed.xml'))

    #doc = xmltodict.parse(input_xml, encoding='utf-8', dict_constructor = dict)

    createNewXML(doc)
    # myfile = open("segunda_division.xml", "wb")  
    # myfile.write(mydata)  
    #mydata.write("segunda_division.xml", encoding="utf-8", method="xml")


def createNewXML(input_xml):
    root = input_xml.getroot()
    # create the file structure
    feed = ET.Element('segunda_division')
    copyright = ET.SubElement(feed, 'copyright')
    image = ET.SubElement(feed,'image')
    imURL = ET.SubElement(image, 'url')
    imLink = ET.SubElement(image, 'link')

    for child_of_root in root:
        if child_of_root.tag == 'title':
            feed.set('title', child_of_root.text)
        if child_of_root.tag == 'pubDate':
            feed.set('published', child_of_root.text)
        if child_of_root.tag == 'language':
            feed.set('lang', child_of_root.text)
        if child_of_root.tag == 'copyright':
            copyright.text = child_of_root.text
        if child_of_root.tag == 'image':
            image.set('title', child_of_root[1].text)
            imURL.text = child_of_root[0].text
            imLink.text = child_of_root[2].text
                
    items = ET.SubElement(feed, 'items')
    for i in root.iter('item'):
        item = ET.SubElement(items, 'item')
        item.set('title', i['title'])
        item.set('description', i['description'])
        item.set('creator', i['dc:creator'])
        link =  ET.SubElement(item, 'link')
        link.text = i['link']
        categories = ET.SubElement(item, 'categories')
        item.text ="<;![CDATA["
        for p in i['content:encoded']:
            item.text += p
        item.text +="]]>;"
        for c in i['category']:
            category = ET.SubElement(categories, 'category')
            category.text = c
    # create a new XML file with the results
    print (ET.tostring(feed, encoding='utf8').decode('utf8'))

    ET.ElementTree(feed).write('segunda_division.xml',encoding="UTF-8",xml_declaration=True)



    


if __name__ == '__main__':
  main()