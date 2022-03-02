def divisors(num):
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
    
