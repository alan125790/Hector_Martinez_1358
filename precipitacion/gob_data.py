#Estado
estado={"id":0,
        "nombre":"",
        "años_precip":[]
        }

#registro de un año
registro_año={
    "año":0,
    "meses":[]
}

#registro de un sólo mes
registro_mes={
    "mes":0,
    "valor":0.0
}

#Lista principal
estados=[]

meses=range(1,13)
años=range(1985,2020)


def init_data():
    print(estado)
    print(años)
