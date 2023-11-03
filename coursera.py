print(type(2))
print(type(2.5))
# <class 'tuple'>
print(type((2, 6, 9)))
# <class 'list'>
print(type([2, 7, 9]))
# variables
base = 3
altura = 2
area = (base * altura)/2
print(area)
# para poder imprir area junto a un string se convierte a string con str()
print("El área es " + str(area))

# declarar funciones con "def"
def area_triangle(base, altura):
    return base*altura/2


area_a = area_triangle(5, 4)
area_b = area_triangle(7, 3)

total_area = area_a + area_b
print("El área total es " + str(total_area))

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds


hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)

# funcion que devuelve None
def greeting(name):
    print("Welcome, " + name)

result = greeting("Christine")
print(result)
# print(result) devuelve None porque no hay un return en la función.

# funciones para reusar código:
def lucky_number(name):
    number = len(name) * 9
    print("Hello " + name + ", your lucky number is " + str(number))

lucky_number("Rafa")
lucky_number("Yolanda")



