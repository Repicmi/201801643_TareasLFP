import xml.dom.minidom
import xml.etree.ElementTree
#def leerXML():
#print("Leyendo datos XML")
#dom = xml.dom.minidom.parse('datosXML.xml')
#print(dom.attribue['nombre1'].value)


#leerXML()
doc = xml.dom.minidom.parse('datosXML.xml')
nombre = doc.getElementsByTagName("nombre")[0]
print(nombre.firstchild.data)
datos = doc.getElementsByTagName("dato")
for dato in datos:
    sid = dato.getAttribute("id")
    nombre = dato.getElementsByTagName("nombre")[0]
    edad = dato.getElementsByTagName("edad")[0]
    apellido = dato.getElementsByTagName("apellido")[0]
    estatura = dato.getElementsByTagName("estatura")[0]
    print("id:%s " % sid)
    print("Nombre:%s " % nombre.firstchild.data," Edad:%s " % edad.firstchild.data," Apellido:%s " % apellido.firstchild.data, " Estatura:%s " % estatura.firstchild.data)
