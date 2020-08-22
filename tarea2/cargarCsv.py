import csv

def leerCSV():
    print("Leyendo archivo CSV")
    with open('datosCSV.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count=0
        for row in csv_reader:
            print(f'Nombre: {row[0] } Edad: {row[1]} Estatura: {row[2]} Color favorito: {row[3]}')
            line_count +=1
