#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xmltodict
import xml.dom.minidom

def main():
    with open('prerromanico.xml', encoding='utf-8') as fd:
        doc = xmltodict.parse(fd.read(), encoding='utf-8', dict_constructor = dict)
        print(doc)
        kmlDoc = createKML(doc)

        kmlFile = open('prerromanico.kml', 'wb')
        kmlFile.write(kmlDoc.toprettyxml('  ', newl = '\n', encoding = 'utf-8'))


def createKML(doc):
  # This constructs the KML document from the CSV file.
  kmlDoc = xml.dom.minidom.Document()
  
  kmlElement = kmlDoc.createElementNS('http://earth.google.com/kml/2.2', 'kml')
  kmlElement.setAttribute('xmlns', 'http://earth.google.com/kml/2.2')
  kmlElement = kmlDoc.appendChild(kmlElement)
  documentElement = kmlDoc.createElement('Document')
  documentElement = kmlElement.appendChild(documentElement)

  for monument in doc['monuments']['monument']:
        name = monument['name']
        description = monument['description']
        coordenates = monument['location']['coordenates']
        latitude = coordenates['latitude']
        longitude = coordenates['longitude']
        altitude = coordenates['altitude']
        placemarkElement = createPlacemark(kmlDoc, name, latitude, longitude, altitude, description)
        documentElement.appendChild(placemarkElement)

  return kmlDoc


def createPlacemark(kmlDoc, name, latitude, longitude, altitude, description):
  # This creates a <Placemark> element for a row of data.
  # A row is a dict.
    placemarkElement = kmlDoc.createElement('Placemark')
    nameElement = kmlDoc.createElement('name')
    nameText = kmlDoc.createTextNode(name)
    nameElement.appendChild(nameText)
    placemarkElement.appendChild(nameElement)

    descriptionElement = kmlDoc.createElement('description')
    descriptionText = kmlDoc.createTextNode(description)
    descriptionElement.appendChild(descriptionText)
    placemarkElement.appendChild(descriptionElement)
    
    pointElement = kmlDoc.createElement('Point')
    placemarkElement.appendChild(pointElement)
    coordinates = longitude +","+latitude + ","+ altitude
    coorElement = kmlDoc.createElement('coordinates')
    coorElement.appendChild(kmlDoc.createTextNode(coordinates))
    pointElement.appendChild(coorElement)
    return placemarkElement
        


if __name__ == '__main__':
  main()