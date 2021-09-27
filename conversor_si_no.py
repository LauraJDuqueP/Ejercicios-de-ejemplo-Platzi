
# pesos = float (input("     Cuantos pesos tienes   "))
# valor_dolares = 3800
# valor_libras_esterlinas = 5200
# valor_euros = 4400 
# print ("""       
#                Bienvenido al conversor de monedas  

#   Podemos convertir tu dinero en Dolares, Libras Esterlinas y Euros""")

 
# moneda = int( input( """
#               ¿A que moneda deseas convertir el dinero?
#                        *  Si es a Dolares marca 1              
#                        *  Si es a Libras Esterlinas marca 2"
#                        *  Si es a Euros marca 3  
#                                        """))
                                                    
                                                         
# if moneda == 1:
#    dolares = (pesos/valor_dolares)
#    dolares = round(dolares, 2)
#    dolares = str (dolares)
#    print ("  Tienes $  " + dolares + "  dolares")
# elif moneda == 2:
#    libras_esterlinas = (pesos/valor_libras_esterlinas)
#    libras_esterlinas = round(libras_esterlinas, 2)
#    libras_esterlinas = str(libras_esterlinas)
#    print ("  Tienes $  " + libras_esterlinas +"  libras esterlinas")
# elif moneda == 3:
#    euros = (pesos/valor_euros)
#    euros = round(euros, 2)
#    euros = str(euros)
#    print ("  Tienes $  " + euros + "  Euros")

# else: print ("  Selecciono un valor no valido")


def conversor(valor_moneda, moneda): 
     pesos = float(input(" Cuantos pesos tienes   "))
     valor = pesos/valor_moneda
     valor = round(valor, 2)
     valor = str(valor)
     print ("tienes $ " + valor + moneda)


print ("""       
            Bienvenido al conversor de monedas  
   Podemos convertir tu dinero en Dolares, Libras Esterlinas y Euros""") 
opccion = int( input( """
              ¿A que moneda deseas convertir el dinero?
                       *  Si es a Dolares marca 1              
                       *  Si es a Libras Esterlinas marca 2"
                        *  Si es a Euros marca 3  
                                        """))
if opccion == 1:
    conversor(3800, "Dolares")
elif opccion == 2:
    conversor (5200, "Libras Esterlinas")
elif opccion == 3:
    conversor (4400, "Euros")
else: print (" Elige la opccion correcta ")
