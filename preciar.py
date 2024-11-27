#!/usr/bin/python3
import sys

print('\n\tCalcula el pasaje de un precio en USD (dólares estadounidenses) por cantidad de libras(LB) a precio en ARS (pesos argentinos) por kilogramo (Kg).\n\n')
# Obtengo datos validos
precio = float(sys.argv[1])
# Valido precio
while (precio < 1):
    precio = float(input('\n\tEl precio en USD debe ser mayor o igual a 1: '))

libras_compradas = float(sys.argv[2])
# Valido cantidad de libras (puede ser 0.25, cuarto de libra pero no cero ni negativa)
while (libras_compradas <= 0):
    libras_compradas = float(input('\nIngrese cuantas libras se pueden comprar con USD %.2f (mas de cero): ' % precio))
# Obtengo precio de ese algo en dolares por libra
resultado_dolares_libra = (precio / libras_compradas)
# Paso precio en dolares a pesos con equivalencia variable que voy actualizando semanalmente
pesos_equivalentes = float(sys.argv[3])
# Convierto a pesos
precio = (precio * pesos_equivalentes)
# Convierto cantidad de libras que se pueden comprar a ese precio de algo a kilogramo
masa_kilos = (libras_compradas * 0.453592)
# Obtengo el precio en pesos por kilo a partir del precio de dolares por libras
resultado_pesos_kilos = (precio / masa_kilos)
# Muestro resultado
print('\n\n\tEl resultado de %.2f USD/LB son %.2f ARS/Kg (a dolar de %.2f ARS).\n' % (resultado_dolares_libra, resultado_pesos_kilos, pesos_equivalentes))
