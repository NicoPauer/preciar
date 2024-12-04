#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float truncar(float num, int lugares)
{
    /* Deveulve un numero real con una cantidad de decimales después del punto. */
    float potencia = pow(10, lugares);

    return (truncf(num * potencia) / potencia);
}

float peso(float medida, float equivalencia_en_otra)
{
    /*
       Deveulve una medida de peso expresada en otra unidad según equivalencia de
       la segunda en la otra unidad.
    */
    return (medida * equivalencia_en_otra);
}

float divisa(float precio, float equivalencia_en_divisa)
{
    /*
        Pasa un precio de una divisa usando su equivalencia a
        otra divisa.
    */
    return truncar((precio * equivalencia_en_divisa), 2);
}

int main(int argc, char * argv[])
{
    /*
        Algoritmo:


        1) Obtener cadena de caracteres unidad_peso_1 en
		   argumento 1.

		2) Obtener cadena de caracteres unidad_peso_2 en
		   argumento 2.

        3) Obtener real precio por cierta cantidad en
		   argumento 3.

        4) Obtener real cierta cantidad de la unidad_peso_1 en
           argumento 4 que se puede obtener por dicho precio.

        5) Obtener real equivalencia entre unidades de peso en
           argumento 5.

        6) Obtener real equivalencia entre divisas en argumento 6.

        7) Obtener cadena de caracteres divisa_1 en argumento 7.

        8) Obtener cadena de caracteres divisa_2 en argumento 8.

        9) Realizar todos los calculos(convertir divisas, convertir peso y su cociente).

        10) Mostrar el resultado.
    */

/* Nombre o simbolo de unidad de peso en la que obtuve la medida*/
	char * unidad_peso_1 = argv[1];
/* Nombre o simbolo de unidad de peso a convertir */
	char * unidad_peso_2 = argv[2];
/* Precio expresado en divisa_1 de cierta_cantidad en unidad_peso_1 a llevar */
	float precio_1 = atof(argv[3]);
/* Media en unidad_peso_1 que se puede llevar por precio_1 */
	float cierta_cantidad = atof(argv[4]);
/* Equivalencia de unidad_peso_1 en unidad_peso_2 */
	float equivalencia_pesaje = atof(argv[5]);
/* Equivalencia de divisa_1 en divisa_2 */
	float equivalencia_divisas = atof(argv[6]);
/* Precio por cada unidad de unidad_peso_2 expresado en divisa_2 */
    float precio_2 = (divisa(precio_1, equivalencia_divisas) / peso(cierta_cantidad, equivalencia_pesaje));
/* Simbolo o nombre de divisa desde cual se requiere convertir */
	char * divisa_1 = argv[7];
/* Simbolo o nombre de la divisa en la que se quiere obtener precio */
	char * divisa_2 = argv[8];
/* Muestro el resultado */
    printf("Si con %s %.2f compro %.2f %s obtengo que por cada %s compro a %s %.2f.\n", divisa_1, precio_1, cierta_cantidad, unidad_peso_1, unidad_peso_2, divisa_2, precio_2);
    return 0;
}
