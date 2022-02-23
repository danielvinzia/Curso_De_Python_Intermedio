def run():
    lista = [1, 2, 3, 4, 5]
    cuadrado = []
    
    for i in lista:
        cuadrado.append(i**2)
    print(cuadrado)
    
    reto = [i**2 for i in lista]
    print(reto)
    
    squares = [i**2 for i in lista]
    print(squares)
    
#    USANDO MAP
    
    squares2 = list(map(lambda x: x**2, lista))
    print(squares2)


if __name__ == '__main__':
    run()
    