Manual de Usuario SimpleQL

Contenido:
* Comandos reconocidos
* Archivos reconocidos para cargarse en la apliación
* Posibles Errores

>Comandos Reconocidos
	Los comandos reconocidos por la aplicación deben de ser ingresados con letras MAYUSCULAS 
seguidos por sus respectivos complementos, los comandos disponibles son

*CARGAR archivo1.json, archivo2.json, .... , archivon.json
	Luego de escribir cargar se deben de escribir los nombres de los archivos json con datos a cargarse
	El programa no tiene un límite para cargar archivos

*SELECCIONAR * o SELECCIONAR dato1, dato2 DONDE dato1="nombre"
	Al ingresar el comando se mostraran los datos solicitados
	el comando tiene 2 formas, se pueden seleccionar todos los datos con *
	se pueden pedir datos especificos con: SELECCIONAR nombre, edad DONDE nombre = "dato especifico"

*SUMA edad o SUMA promedio
	El comando suma todas las edades o todos los promedios cargados con los archivos

*MAXIMO edad o MAXIMO promedio
	El comando ordena los datos y muestra la edad o el promedio mayor de los datos ingresados

*MINIMO edad o MINIMO promedio
	EL comando ordena los datos y muestra la edad o el promedio menor de los demas datos ingresados

*CUENTA 
	Muestra en pantalla el total de datos registrados

*REPORTAR 1
	Genera un reporte en HTML con todos los datos ingresados

>Archivos reconocidos por la aplicación
	Todos los archivos que se deseen cargar deben estar en formato .json y solo deben contener los datos
	nombre, edad, promedio y activo (falso o verdadero)

> Posibles errores
	Por fallos técnicos solo se pueden seleccionar todos los datos al mismo tiempo, se buscará una solución 
	al problema 