def run():
    palindrome = lambda string: string == string[::-1]
    
    print(palindrome('ana'))
    
    """ ES LO MISMO QUE LO QUE VOY A ESCRIBIR AHORA """

    def palindrome2(string):
        return string == string[::-1]
    
    print(palindrome2('ana'))


if __name__ == '__main__':
    run()
    