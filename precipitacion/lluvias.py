import xlrd
data=[]
for anio in range(1985,2019):
    anio_lista=[]
    archivo=xlrd.open_workbook(filename="./Precipitacion/"+str(anio)+'Precip.xls')
    hoja=archivo.sheet_by_index(0)
    for estado in range (2,35):
        mes_lista=[]
        for mes in range(1,14):
            mes_lista.append(hoja.cell_value(estado,mes))
        anio_lista.append(mes_lista)
    data.append(anio_lista)
    
print(data)

print("Estados:\n Aguascalientes = 1 \n Baja California = 2 \n Baja California Sur = 3 \n"+
          " Campeche = 4 \n Coahuila = 5 \n Colima = 6 \n Chiapas = 7 \n Chihuahua = 8\n"+
          " CDMX = 9 \n Durango = 10 \n Guanajuato = 11 \n Guerrero = 12 \n Hidalgo = 13 \n"+
          " Jalisco = 14 \n EDOMEX = 15 \n Michoacan = 16 \n Morelos = 17 \n Nayarit = 18 \n"+
          " Nuevo Leon = 19 \n Oaxaca = 20 \n Puebla = 21 \n Querétaro = 22 \n Quintana Roo = 23 \n"+
          " San Luis Potosi = 24 \n Sinaloa = 25 \n Sonora = 26 \n Tabasco = 27 \n Tamaulipas  = 28 \n"+
          " Tlaxcala = 29 \n Veracruz = 30 \n Yucatán = 31 \n Zacatecas = 32")
estado=int(input("Ingrese estado(1-32)(33 nacional): "))
anio=int(input("Ingrese el año(1985-2019):"))
print("En caso de 2019 unicamente hasta junio")
mes=int(input("Ingrese el mes(1-12)(13 es anual): "))

print(f"el promedio mensual es:{data[anio-1985][estado-1][mes-1]}")

