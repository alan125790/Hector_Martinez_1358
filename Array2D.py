class Array2D:
    def __init__(self, rows, cols):
        self.__data=[]
        self.__row=rows
        self.__col=cols
        for row in range(rows):
            tmp=[]
            for col in range(cols):
                tmp.append(None)
            self.__data.append(tmp)

    def to_string(self):
        print(self.__data)

    def get_num_rows(self):
        return self.__row

    def get_num_cols(self):
        return self.__col

    def clearing(self, value):
        for row in range(self.__row):
            for col in range(self.__col):
                self.__data[row][col]=value

    def set_item(self, r, c, valor):
        if (r>=0 and r<self.__row)and(c>=0 and c<self.__col):
            self.__data[r][c]=valor


    def get_item(self, r, c):
        if (r>=0 and r<self.__row)and(c>=0 and c<self.__col):
            return self.__data[r][c]






def main():
    Arreglo=Array2D(5,5)
    Arreglo.to_string()
    print(f"Numero de renglones: {Arreglo.get_num_rows()}")
    print(f"Numero de columnas: {Arreglo.get_num_cols()}")
    Arreglo.clearing(1)
    Arreglo.to_string()
    Arreglo.set_item(2,3,10)
    Arreglo.get_item(2,3)
    Arreglo.to_string()

main()
