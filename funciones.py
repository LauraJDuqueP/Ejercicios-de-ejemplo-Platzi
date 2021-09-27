# def vamos(): 
#    print("vamos que si se puede")
#    print("siempre estudia algo nuevo")


# vamos()
# vamos()
# vamos()

# print ("mensaje especial:")
# print ("¡Estoy aprendiendo a usar funciones!")
# print ("mensaje especial:")
# print ("¡Estoy aprendiendo a usar funciones!")
# print ("mensaje especial:")
# print ("¡Estoy aprendiendo a usar funciones!")



"""
----------------------------------
opcion = int(input("Elige una opcion (1, 2, 3):  "))
if opcion == 1:
    print ("hola")
    print ("¿Cómo estas?")
    print ("Elegiste la opción 1")
    print ("Adios")
elif opcion == 2:  
    print ("hola")
    print ("¿Cómo estas?")
    print ("Elegiste la opción 2")
    print ("Adios")
elif opcion == 3:
    print ("hola")
    print ("¿Cómo estas?")
    print ("Elegiste la opción 3")
    print ("Adios")
else:
    print ("Escribe la opcion correcta")"""

def conversacion(mensaje):
    print ("hola")
    print ("¿Cómo estas?")
    print (mensaje)
    print ("Adios")

opcion = int(input("Elige una opción (1, 2, 3): "))
if opcion == 1:
    conversacion("Elegiste la opción 1")
elif opcion == 2:
    conversacion("Elegiste la opción 2")
elif opcion == 3:
    conversacion("Elegiste la opción 3")
else:
    print ("Escribe la opción correcta") 

    