import cargarJson
import cargarCsv

op=1
while(op != 4):
    if op == 1:
        print("Archivo Json:")
        dict = cargarJson.leerJson()
        for element in dict:
            print(element)
        input("Enter para continuar")
        op +=1
    elif op == 2:
        cargarCsv.leerCSV()
        input("Enter para continuar")
        op += 1
    elif op == 3:
        print("Tuve problemas tratando de leer el XML, solo creé el archivo XML")
        input("Enter para continuar")
        op += 1
    elif op == 4:
        print("gracias vuelva pronto")