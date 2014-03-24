#coding:utf-8

import requests
from lxml import etree

respuesta = requests.get("http://open.mapquestapi.com/xapi/api/0.6/*[bbox=2.79,41.96,2.81,41.98]")

arbol_xml = etree.fromstring(respuesta.text.encode("utf-8"))

#print respuesta.text

numero_inodos = len(arbol_xml.findall("node"))

print "El numero de inodos del recuadro es: ",numero_inodos


