#Variables

my_variable="My String variable"
print(my_variable)

my_int_variable=5
print(my_int_variable)

my_int_to_str_variable=str(my_int_variable)
print(my_int_to_str_variable)

my_boolean_variable=True
print(my_boolean_variable)

#Variables en una sola linea

name,surname,alias,age="Juan","Mayorga","Jeiden",23
print("Me llamo:",name,surname,"Mi edad es:",age,"Mi alias es:",alias)

#Concatenacion de cadenas
print(my_variable,my_int_variable,my_boolean_variable)

#Funciones del sistema

#len
print(len(my_variable))

#input
name=input("Cuan es tu nombre? \n")
print(name) 

#Cambiamos su tipo
name=23
age="Juan"
print(name)
print(age)

#¿Forzamos el tipado?
address:str="My dirreccion"
print(address)
address=23
print(type(address))