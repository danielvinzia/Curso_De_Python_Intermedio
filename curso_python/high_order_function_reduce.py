from functools import reduce

def run():
    my_list = [2, 2, 2, 2, 2]
    
    all_multiplied = 1
    
    for i in my_list:
        all_multiplied = all_multiplied *i
    
    print(all_multiplied)

#   USANDO REDUCE
    all_multiplied2 = reduce(lambda a, b: a*b, my_list)
#   LA MULTIPLICACION QUE HACE ES: 2*2, 4*2, 8*2, *16*2, PORQUE EL PRIMER ELEMENTO DE LA
#   MULTIPLICACION ES EL RESULTADO DE LA ANTERIOR
    print(all_multiplied2)




if __name__ == '__main__':
    run()
    