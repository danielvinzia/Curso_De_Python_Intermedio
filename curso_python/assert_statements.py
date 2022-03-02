"""  EXPLICACION DE ASSERT  """
# def palindrome(string):
#     assert len(string) > 0, "No se puede ingresar una cadena vacia"
#     return string == string[::-1]


# def run():
#     try:
#         print(palindrome(""))
#     except TypeError:
#         print("Solo se pueden ingresar strings")


# if __name__ == '__main__':
#     run()


def divisors(num):    
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    num = input("Enter a number: ")
    assert num.isnumeric(), "Debes ingresar un numero"
    """ agregrue la linea del reto pero hay que sacar la linea anterior 
    para que funcione ya que la linea anterior es multifuncion """
    # assert int(num) > 0, "Debes ingresar numeros positivos"
    print(divisors(int(num)))
    print("Finish the Daniel's program")


if __name__ == '__main__':
    run()
