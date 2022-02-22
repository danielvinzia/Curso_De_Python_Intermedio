import math

def run():
    my_dict2 = {i:math.sqrt(i) for i in range(1, 1001)}
    
    for key, value in my_dict2.items():
        print("la raiz cuadrada de", key, "es", round(value,2))


if __name__ == '__main__':
    run()
    