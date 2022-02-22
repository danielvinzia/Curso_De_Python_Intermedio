def run():
    lista_dani = []
    
    for i in range(1, 101):
        a = i*i
        lista_dani.append(a)
    
    l = 1
    for item in lista_dani:
        print(l, "al cuadrado es", item)
        l += 1



if __name__ == '__main__':
    run()