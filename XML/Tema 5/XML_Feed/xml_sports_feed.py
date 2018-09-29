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
    myfile = open("segunda_division.xml", "w")  
    myfile.write(mydata)  

def createNewXML(input_xml):
    # create the file structure
    root = input_xml['rss']['channel']
    feed = ET.Element('feed')
    feed.set('title', root['title'])
    feed.set('link', root['link'])
    items = ET.SubElement(feed, 'items')
    for i in root['item']:
        item = ET.SubElement(items, 'item')
        item.set('title', i['title'])
        
        categories = ET.SubElement(item, 'categories')
        
        for c in i['category']:
            category = ET.SubElement(categories, 'category')
            category.text = i['category']



        
    item1 = ET.SubElement(items, 'item')
    item2 = ET.SubElement(items, 'item')
    
    item1.set('name','item1')  
    item2.set('name','item2')  
    item1.text = 'item1abc'  
    item2.text = 'item2abc'

    # create a new XML file with the results
    mydata = ET.tostring(feed)  
    
    return mydata


    


if __name__ == '__main__':
  main()