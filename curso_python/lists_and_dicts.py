def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Daniel", "lastname": "Vinzia"}
    
    super_list = [
        {"firstname": "Daniel", "lastname": "Vinzia"},
        {"firstname": "Miguel", "lastname": "Vinzia"},
        {"firstname": "Macarena", "lastname": "Garcia"},
        {"firstname": "Santiaguito", "lastname": "Sandoval"},
        {"firstname": "Juan", "lastname": "Toledo"},
    ]
    
    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums":[1.1, 4.5, 6.43]
    }
    
    for key, value in super_dict.items():
        print(key, "-", value)
    
    for item in super_list:
        print("Nombre:", item["firstname"], " - ", "Apellido:", item["lastname"])


if __name__ == '__main__':
    run()
    