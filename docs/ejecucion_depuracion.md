# Ejecución y Depuración

En esta sección se documenta la ejecución de la aplicación, los problemas detectados y las soluciones aplicadas.

## Ejecución de la aplicación

Para ejecutar la aplicación en un entorno local:

1. Crear un entorno virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Ejecutar tests unitarios:

```bash
PYTHONPATH=src python3 test/test_lavadero_unittest.py -v
```

---

## Problemas detectados y soluciones

1. Método `ejecutar_y_obtener_fases` no tabulado:

**Problema**: Al principio el método no estaba correctamente indentado dentro de la clase Lavadero.

**Solución**: Se corrigió la indentación para que el método formara parte de la clase.

2. Acceso a atributos privados:

**Problema**: El método `ejecutar_y_obtener_fases` accedía a self.fase y self.ocupado directamente, provocando errores en los tests.

**Solución**: Se cambió el acceso a `self.__fase` y `self.__ocupado` dentro del método.

3. Orden de cálculo de `_cobrar()`:

**Problema**: Los ingresos se calculaban en un orden incorrecto, afectando los tests de ingresos.

**Solución**: Se reordenó la suma de costes según las opciones seleccionadas:

```python
if self.__prelavado_a_mano:
    coste_lavado += 1.50 

if self.__secado_a_mano:
    coste_lavado += 1.00 

if self.__encerado:
    coste_lavado += 1.20
```

4. Manejo de fases de secado y encerado

**Problema**: No se consideraban correctamente los bloques __secado_a_mano y __encerado al avanzar fases.

**Solución**: Se añadieron condiciones if ... else ... en el bloque de avanzarFase para manejar todos los flujos correctamente.

---

## Resultados de los test

```bash
test10_flujo_con_prelavado (__main__.TestLavadero.test10_flujo_con_prelavado)
Test 10: ... ok
test11_flujo_con_secado_mano (__main__.TestLavadero.test11_flujo_con_secado_mano)
Test 11: ... ok
test12_flujo_completo (__main__.TestLavadero.test12_flujo_completo)
Test 12: ... ok
test13_flujo_prelavado_y_secado (__main__.TestLavadero.test13_flujo_prelavado_y_secado)
Test 13: ... ok
test14_flujo_completo_finalizacion (__main__.TestLavadero.test14_flujo_completo_finalizacion)
Test 14: ... ok
test1_estado_inicial_correcto (__main__.TestLavadero.test1_estado_inicial_correcto)
Test 1: ... ok
test2_excepcion_encerado_sin_secado (__main__.TestLavadero.test2_excepcion_encerado_sin_secado)
Test 2: ... ok
test3_no_se_puede_iniciar_dos_lavados (__main__.TestLavadero.test3_no_se_puede_iniciar_dos_lavados)
Test 3: ... ok
test4_ingresos_prelavado (__main__.TestLavadero.test4_ingresos_prelavado)
Test 4: ... ok
test5_ingresos_secado_mano (__main__.TestLavadero.test5_ingresos_secado_mano)
Test 5: ... ok
test6_ingresos_secado_y_encerado (__main__.TestLavadero.test6_ingresos_secado_y_encerado)
Test 6: ... ok
test7_ingresos_prelavado_y_secado (__main__.TestLavadero.test7_ingresos_prelavado_y_secado)
Test 7: ... ok
test8_ingresos_completo (__main__.TestLavadero.test8_ingresos_completo)
Test 8: ... ok
test9_flujo_rapido_sin_extras (__main__.TestLavadero.test9_flujo_rapido_sin_extras)
Test 9: ... ok
test_reseteo_estado_con_terminar (__main__.TestLavadero.test_reseteo_estado_con_terminar)
Test: Verifica que terminar() resetea todas las flags y el estado. ... ok
```
