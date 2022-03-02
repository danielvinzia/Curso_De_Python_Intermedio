def divisors(num):
    try:
        if num < 0:
            raise ValueError("No se pueden ingresar numeros negativos")
        return
    except ValueError as cualquierValor:
        print(cualquierValor)
        
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    try:
        num = int(input("Enter a number: "))
        print(divisors(num))
        print("Finish the Daniel's program")
    except ValueError:
        print("Debes ingresar un numero")


if __name__ == '__main__':
    run()
    
