#!/usr/bin/python3
import sys, math

def truncado(num:float, lugares:int) -> float:
    '''
        Devuelve un numero real truncado a n
        lugares después de la parte entera.
    '''
    potencia = (10 ** lugares)
    return (math.trunc(num * potencia) / potencia)

def peso(medida:float, equivalencia:float) -> float:
    '''
        Convierte una medida expresada en otra unidad con
        su equivalencia a la unidad de peso buscada
    '''
    return (medida * equivalencia)

def divisa(precio:float, tipo_de_cambio:float) -> float:
    '''
        Convierte un precio expresado en una divisa con
        su tipo de cambio a otra.
    '''
    return truncado((precio * tipo_de_cambio), 2)

def argumentos(posicion:int) -> float:
    '''
        Obtiene argumento real en una posicion n
        de la linea de comandos.
    '''
    return truncado(float(sys.argv[posicion]), 2)

def argu_text(posicion:int) -> str:
    '''
        Obtiene argumentos de tipo texto
        en una posicion n.
    '''
    return str(sys.argv[posicion])
# Implemento algoritmo
unidad_peso_entrada = argu_text(1)

unidad_peso_salida = argu_text(2)

precio = argumentos(3)

pesa = argumentos(4)

equivalencia_pesaje = argumentos(5)

equivalencia_divisas = argumentos(6)

divisa_entrada = argu_text(7)

divisa_salida = argu_text(8)
# Muestro el resultado
print(f'\n\t{pesa} {unidad_peso_entrada} a {divisa_entrada} {precio} son {divisa_salida} {truncado((divisa(precio, equivalencia_divisas) / peso(pesa, equivalencia_pesaje)), 2)} por cada {unidad_peso_salida} a {divisa_salida} {equivalencia_divisas} por cada {divisa_entrada}.\n')
