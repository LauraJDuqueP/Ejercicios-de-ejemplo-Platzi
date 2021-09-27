pesos = input ("¿Cúantos pesos colombianos tienes?: ")
pesos = float(pesos)
valor_dolar = 3875 
dolares = (pesos/valor_dolar) 
dolares = round(dolares, 2)
dolares = str(dolares)
valor_libras = 5221 
libra_esterlina = (pesos/valor_libras)
libra_esterlina = round(libra_esterlina, 2)
libra_esterlina = str(libra_esterlina)

print("Tienes  $" + dolares +   "  dolares"  )
print ("Tienes $" + libra_esterlina +   "  libras esterlinas")
