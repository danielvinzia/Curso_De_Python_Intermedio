"""  TRY Y EXCEPT   """

# def palindrome(string):
#     return string == string[::-1]


# def run():
#     try:
#         print(palindrome(1))
#     except TypeError:
#         print("Solo se pueden ingresar strings")


# if __name__ == '__main__':
#     run()


"""  RAISE  """

def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError("No se puede ingresar una cadena vacia")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False


def run():
    try:
        print(palindrome(""))
    except TypeError:
        print("Solo se pueden ingresar strings")


if __name__ == '__main__':
    run()


"""  FINALLY  """

# try:
#   f = open("archivo.txt")
### hacer cualquier cosa con nuestro archivo
# finally:
#   f.close()
