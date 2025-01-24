"""
DECORADOR DE SUPERPODERES
Objetivo: Crear un decorador que otorgue superpoderes a personajes de videojuegos y les permita realizar acciones especiales.
"""
registered_names = ['Artemis', 'Nina', 'Myth']

# Decorador para comprobar que el nombre no haya sido registrado previamente:
def character_name(func):
    def wrapper(name, action):
        if name in registered_names:
            print(f'El nombre "{name}" ya se encuentra registrado. Por favor, elija un nuevo nombre.')
            return
        if name not in registered_names:
            registered_names.append(name)
            print(f'¡El nombre "{name}" ha sido registrado con éxito!')
        return func(name, action)
    return wrapper

# Función que contiene las acciones básicas del personaje:
def character_actions(name, action):
    if action == 'Caminar':
        print(f'{name} está caminando, pero se detiene más adelante.')
    elif action == 'Correr':
        print(f'{name} empieza a correr, pero cae al suelo al tropezar con una piedra en el camino. Se levanta nuevamente para continuar su camino.')
    elif action == 'Comer':
        print(f'{name} tiene hambre. Por suerte, encuentra un árbol de manzanas a su paso, por lo que toma una y la come.')
    elif action == 'Saltar':
        print(f'{name} empieza a saltar como si no hubiese un mañana, hasta que se cansa y deja de hacerlo.')

# Decorador para agregar superpoderes al personaje:
def superpowers(func):
    def wrapper(name, action):
        if action == 'Atacar':
            print(f'{name} está atacando con su superpoder "Ráfaga de furia".')
        elif action == 'Descansar':
            print(f'{name} ha decidido descansar para regenerar energía.')
        return func(name, action)
    return wrapper

# Función principal (acciones básicas del personaje) que utiliza las funciones «character_name» y «superpowers» como decoradores:
@character_name
@superpowers
def performing(name, action):
    character_actions(name, action)

# Muestro por consola las impresiones definidas en las funciones decoradoras de la función madre:

# performing('', '')
performing('Alyssa', 'Saltar')
