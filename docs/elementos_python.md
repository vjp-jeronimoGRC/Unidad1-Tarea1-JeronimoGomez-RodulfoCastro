# Elementos de Python

La aplicación está desarrollada en **Python** siguiendo un enfoque de **programación orientada a objetos (OOP)**.  

La clase principal es `Lavadero`, que modela el comportamiento de un túnel de lavado de coches.  

## Elementos utilizados

En esta clase se utilizan:

- **Clases y encapsulación:** Atributos privados (`__atributo`) y métodos para controlar el estado interno.  
- **Propiedades (`@property`)** para acceso seguro a los atributos.  
- **Métodos públicos y privados** para separar la lógica de negocio de utilidades internas.  
- **Excepciones (`ValueError`, `RuntimeError`)** para validar reglas de negocio.  
- **Constantes de clase** para representar los estados (fases) del lavadero.  

## Clase Lavadero

Define las fases del lavado mediante constantes de clase:

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
---

## Métodos principales

- `hacerLavado(prelavado_a_mano, secado_a_mano, encerado)` -> Inicia un ciclo de lavado y valida las reglas de negocio.

- `avanzarFase()` -> Controla la transición entre las fases según las opciones seleccionadas.

- `_cobrar()` -> Calcula los ingresos según las opciones activadas.

- `terminar()` ->Restablece el estado del lavadero a inactivo.

- `imprimir_fase() / imprimir_estado()` Métodos auxiliares para visualizar el estado actual del lavadero.
