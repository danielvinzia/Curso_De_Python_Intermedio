def run():
    cubitos = {}
    
    for i in range(1, 101):
        if i % 3 != 0:
            cubitos[i] = {i**3}
    
    for key, value in cubitos.items():
        print("el cubo de", key, "es", value)


if __name__ == '__main__':
    run()
    