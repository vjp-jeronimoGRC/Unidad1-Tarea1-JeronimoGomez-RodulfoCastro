## Elementos de Python

La aplicación está desarrollada en Python siguiendo un enfoque de programación orientada a objetos (OOP).

La clase principal es `Lavadero`, que modela el comportamiento de un túnel
de lavado de coches. En esta clase se utilizan los siguientes elementos de Python:

- Clases y encapsulación mediante atributos privados (`__atributo`)
- Métodos públicos y privados
- Propiedades (`@property`) para acceso controlado al estado interno
- Uso de excepciones (`ValueError`, `RuntimeError`)
- Constantes de clase para representar los estados (fases) del lavadero

### Clase Lavadero

La clase `Lavadero` define las fases del lavado mediante constantes de clase,
por ejemplo:

```python
FASE_INACTIVO = 0
FASE_COBRANDO = 1
FASE_PRELAVADO_MANO = 2
FASE_ECHANDO_AGUA = 3
FASE_ENJABONANDO = 4
FASE_RODILLOS = 5
FASE_SECADO_AUTOMATICO = 6
FASE_SECADO_MANO = 7
FASE_ENCERADO = 8
```

### Métodos principales

- `hacerLavado()` -> Inicia un ciclo de lavado y verifica las reglas del negocio de lavado de ropa.
- `avanzarFase()` -> Controla la transición entre las distintas fases.
- `_cobrar()` -> Calcula los ingresos del lavado según las opciones introducidas.
- `terminar()` -> Restablece el estado del lavadero al finalizar el proceso.
---
### Sandboxing

Para arrancar las pruebas en Sandboxing primero deberemos crear el entorno virtual con el siguiente comando:

```bash
python3 -m venv venv
source venv/bin/activate

---
### Resultados de los test unitarios

Al final de las pruebas una vez desarrolladas ejecutaremos lo siguiente:

```bash
PYTHONPATH=src python3 test/test_lavadero_unittest.py -v
```
Y si todos los test están correctos en la terminal veremos los siguiente:

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
---
### Soluciones de código 

1. Aplicar una tabulación en la declaración del método `ejecutar_y_obtener_fases`.
2. Acceder a las propiedades privadas dentro del método `ejecutar_y_obtener_fases`: 
	- `prelavado`
	- `secado_mano`
	- `encerado`
3. Todos verifican que los ingresos se calculan correctamente según las opciones seleccionadas. Ok tras mantener el método `_cobrar` 
   y acceder a propiedades privadas correctamente.
4. En el método cobrar se debe cambiar el orden de los cobros del lavado y debe quedar así:
```python
	if self.__prelavado_a_mano:
            coste_lavado += 1.50 
        
        if self.__secado_a_mano:
            coste_lavado += 1.00 
            
        if self.__encerado:
            coste_lavado += 1.20
```

---
### requeriments.txt

En este proyecto no va a hacer falta instalar ciertos requerimientos ya que el `unittest` ya está incluido en **Python**


