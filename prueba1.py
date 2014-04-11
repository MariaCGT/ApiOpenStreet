#coding:utf-8

import requests
from lxml import etree
from bottle import request, get, post, run, debug

#respuesta = requests.get("http://open.mapquestapi.com/xapi/api/0.6/*[bbox=2.79,41.96,2.81,41.98]")

#arbol_xml = etree.fromstring(respuesta.text.encode("utf-8"))

#numero_inodos = len(arbol_xml.findall("node"))



#print "El numero de inodos del recuadro es: ",numero_inodos

@get('/box')
def box():
    return '''
        <form action="/box" method="post">
			 Define el área.
			 Izquierda:<input name="lad_iz" type="text" /> \n
             Abajo: <input name="abajo" type="text" />
             Derecha: <input name="lad_dr" type="text" />
             Arriba: <input name="arriba" type="text" />
            <input value="" type="submit" />
        </form>
	'''
@post('/box')
def box():
	lad_iz = request.forms.get('lad_iz')
	abajo = request.forms.get('abajo')
	lad_dr = request.forms.get('lad_dr')
	arriba = request.forms.get('arriba')
	return'''
		
		'''
		
	
 

run(host='localhost', port=8080)
