import re, json, os
opcion = ""
datos_cargados = []
cantidad_cargada = 0
maximo = []
minimo = []
suma = 0
cuenta_cargada = 0
while opcion != "SALIR":
    print("==|==|==|==|==|==|==|==|==|==|")
    print("Bienvenido!")
    print("Ingrese el comando deseado: (Escriba AYUDA para mas informacion)")
    opcion = input(">... ")
    opcion = re.sub(",", "", opcion)
    opcion = re.split("\s", opcion)

    if opcion[0] == "CARGAR":
        print("Cargando archivos...")
        for y in opcion:
            if y == "CARGAR":
                continue
            with open(y, 'r') as f:
                z = json.load(f)
                cantidad_cargada = cantidad_cargada + 1
                datos_cargados.append(z)
        print("archivos cargados correctamente!")
    elif opcion[0] == "SELECCIONAR":
        print("Datos Seleccionados:")
        size = len(opcion)

        if opcion[1] =="*":
            print("Seleccionados todos los datos:")
            for i in range(0,len(datos_cargados)):
                for data in datos_cargados[i]:
                    print("=|=|=|=|=|=|=|=|=|=|=|=|")
                    print("Dato cargado:")
                    print("Nombre: %s" % data['nombre'])
                    print("Edad: %s" % data['edad'])
                    print("Activo: %s" % data['activo'])
                    print("Promedio: %s" % data['promedio'])
        else:
            print("Actualmente no se pueden seleccionar datos de forma individual")

    elif opcion[0] == "SUMA":
        if opcion[1] == "edad":
            suma = suma * 0
            for i1 in range(0, len(datos_cargados)):
                for data1 in datos_cargados[i1]:
                    suma = suma + data1["edad"]
            print("La suma de edades es : %d" % suma)
        elif opcion[1] == "promedio":
            suma = suma * 0
            for i2 in range(0, len(datos_cargados)):
                for data2 in datos_cargados[i2]:
                    suma = suma + data2["promedio"]
            print("La suma de promedios es %d" % suma)
        else:
            print("SUMA solo puede operar con la edad o el promedio!")

    elif opcion[0] == "MAXIMO":
        if opcion[1] == "edad":
            for m1 in range (0, len(datos_cargados)):
                for datam1 in datos_cargados[m1]:
                    maximo.append(datam1["edad"])
            print("La edad máxima es : %d" % (max(maximo)))
            maximo.clear()
        elif opcion[1] == "promedio":
            for m2 in range (0, len(datos_cargados)):
                for datam2 in datos_cargados[m2]:
                    maximo.append(datam2["promedio"])
            print("El promedio Máximo es : %d" % (max(maximo)))
            maximo.clear()
        else:
            print("MAXIMO solo funciona con edad o promedio!")

    elif opcion[0] == "MINIMO":
        if opcion[1] == "edad":
            for min1 in range (0,len(datos_cargados)):
                for datamin1 in datos_cargados[min1]:
                    minimo.append(datamin1["edad"])
            print("La edad mínima es: %d" % (min(minimo)))
            minimo.clear()

        if opcion[1] == "promedio":
            print("promedio")
            for min2 in range (0, len(datos_cargados)):
                for datamin2 in datos_cargados[min2]:
                    minimo.append(datamin2["promedio"])
            print("El promedio mínimo es : %d" % (min(minimo)))
            minimo.clear()
        else:
            print("MINIMO solo funciona con edad o promedio!")

    elif opcion[0] == "SALIR":
        print("CERRANDO PROGRAMA...")
        break
    elif opcion[0] == "REPORTAR":
        contados = 0
        for contar in range (0, len(datos_cargados)):
            contados = contados + (len(datos_cargados[contar]))
        if int(opcion[1]) > contados:
            print("No hay suficientes datos para reportar, vuelva a intertar con menos")
        else:
            print("Creando archivo HTML con cantidad de datos indicada. Espere...")
            clase = "tabla"
            f = open('reporte.html', 'w')
            f.write("<html>")
            f.write("<head> <title> Reporte de datos SimpleQL </title> <link rel='stylesheet' href='CSS/style.css'> </head>")
            f.write("<body>")
            f.write("<h3 class='titulo'>Resumen de datos ingresados vía Python:</h3>")
            f.write("<font size=3>")
            f.write("<table class='tabla'")
            f.write("<tr>")
            f.write("<th>Nombre</th>")
            f.write("<th>Edad</th>")
            f.write("<th>Activo</th>")
            f.write("<th>Promedio</th>")
            f.write("</tr>")
            for report in range (0, len(datos_cargados)):
                for reported in datos_cargados[report]:
                    f.write("<tr>")
                    f.write("<td> %s" % reported['nombre'] + "</td>")
                    f.write("<td> %s" % reported['edad'] + " </td>")
                    f.write("<td> %s" % reported['activo'] + " </td>")
                    f.write("<td> %s" % reported['promedio'] + " </td>")
                    f.write("</tr>")
            f.write("</table>")
            f.write("</body>")
            f.write("</html>")
            f.close()
            os.system("start reporte.html")
    elif opcion[0] == "AYUDA":
        print("Comandos reconocidos:")
        print("CARGAR") #ya
        print("SELECCIONAR") #ya
        print("--> *") #ya
        print("--> DONDE")#holy shit esto si esta jodido xd
        print("MAXIMO") #ya
        print("MINIMO") #ya
        print("SUMA") #ya
        print("CUENTA") #ya
        print("REPORTAR") #ya
        print("SALIR") #ya

    elif opcion[0] == "CUENTA":
        for cuenta in range (0, len(datos_cargados)):
            cuenta_cargada = cuenta_cargada + (len(datos_cargados[cuenta]))
        print("En total se han cargado: %d" % cantidad_cargada + " archivos")
        print("con un total de: %d" % cuenta_cargada + " Registros en total")
        cuenta_cargada = cuenta_cargada * 0

    else:
        print("COMANDO NO CONOCIDO")