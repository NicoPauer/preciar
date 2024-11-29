// Relativas a cuestiones tecnicas
use std :: env;

fn truncado(num:f32, lugares:u32) -> f32
{ // Trunca a tantos lugares un numero real
    // Calculo numero para determinar lugares
    let mut potencia:f32 = 1.0;

    for _ in 1..=lugares
    {
        potencia *= 10.0;
    }

    // Devuelve un numero con cierta cantidad de lugares luego del punto
    return f32::trunc(num * potencia) / potencia;
}

fn argumentos(seleccionar:usize) -> f32
{
    // Retorna el argumento pasado por linea de comandos de 1 a n
    let argu:Vec<String> = env :: args().collect();

    let mut devuelto:f32 = argu[seleccionar].clone().parse().expect("\n\t[VALOR MAL PASADO POR LINEA DE COMANDOS]\t\n\n");

    if devuelto < 0.0
    { // corrijo valores negativos
        devuelto = -devuelto;
    }
    // Devuelvo resultado truncado a 2 decimales
    return truncado(devuelto, 2);
}

fn argu_text(seleccionar:usize) -> String
{
    // Retorna el argumento pasado por linea de comandos de tipo texto
    let argu:Vec<String> = env :: args().collect();

    let devuelto:String = argu[seleccionar].clone().parse().expect("\n\t[VALOR MAL PASADO POR LINEA DE COMANDOS]\t\n\n");

    return devuelto;
}
// Relativas al algoritmo
fn libras_kilogramos(medida:f32) -> f32
{
    // Convierte medida en libras a medida en kilogramos
    return medida * 0.453592;
}

fn convertir_divisa(precio:f32, equivalencia:f32) -> f32
{
/*

    Convierte una divisa usando la equivalencia en la otra divisa:

        Divisa A equivale a tanto de divisa B, convertir de divisa A a divisa B.
*/
    return truncado(precio * equivalencia, 2);
}
// Programa principal
fn main()
{
// Paso 1: Obtener precio y cuantas libras compra de algo
    let precio:f32 = argumentos(1);

    let peso_libras:f32 = argumentos(2);
// Paso 2: Pasar medida en libras a kilogramos
    let peso_kilogramos:f32 = libras_kilogramos(peso_libras);
// Paso 3: Pasar precio a divisa requerida
    let equivalencia_a_divisa_requerida:f32 = argumentos(3);
// Adicional en Rust: obtengo divisas a usar con destructuring
    let (divisa_1, divisa_2) = (argu_text(5), argu_text(4));
    let conversion:f32 = convertir_divisa(precio, equivalencia_a_divisa_requerida);
// Paso 4: Dividir entre conversion a divisa requerida y medida en kilogramos
    let resultado:f32 = truncado(conversion / peso_kilogramos, 2);
// Muestro el resultado
    println!("\t{divisa_1} {precio} por {peso_libras} Libras(LB), tomando {divisa_1} 1 a {divisa_2} {equivalencia_a_divisa_requerida}, es {divisa_2} {resultado} por kilo(Kg).")
}
