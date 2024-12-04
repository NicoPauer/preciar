#!/usr/bin/bash
# Dice que se probara
echo "" && echo "Prueba todos los scripts [preciar] para calcular diferencias entre precios." && echo "" && sleep 1
# Contador de segundos, espero un tiempo, limpio pantalla y vuelvo a imprimir
echo "" && echo "5 segundos" && sleep 1 && clear && echo "4 segundos" && sleep 1 && clear && echo "3 segundos" && sleep 1 && clear && echo "2 segundos" && sleep 1 && clear && echo "1 segundo" && sleep 1 && clear && echo "A Probar..." && echo "" && sleep 3

# todos deben dar: 3571.42 ARS, dolara a 1000 y vender 1 onza por kilogramos

echo "Pruebo Python..." && echo "" && sleep 1
chmod +x preciar.py && echo "" && echo "Interpretacion:" && echo "" && time -p ./preciar.py "Onzas" "Kilogramos" "1" "1" "0.283495" "1000" "USD" "ARS" && sleep 3
echo "" && echo "Pruebo Rust..." && echo "" && sleep 1
echo "" && echo "Compilacion: " && echo "" && time -p rustc preciar.rs -o preciar && echo "" && echo "Ejecucion: " && time -p preciar "Onzas" "Kilogramos" "1" "1" "0.283495" "1000" "USD" "ARS" && sleep 3
echo "" && echo "Pruebo C..." && echo "" && sleep 1
echo "" && echo "Compilacion: " && echo "" && time -p gcc preciar.c -o preciar_c -lm && time -p ./preciar_c "Onzas" "Kilogramos" "1" "1" "0.283495" "1000" "USD" "ARS" && sleep 3
