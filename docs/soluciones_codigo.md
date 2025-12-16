# Soluciones de Código

En esta sección se documentan los problemas detectados en el código fuente de la clase `Lavadero` y las soluciones aplicadas.

## Problema 1: Método `ejecutar_y_obtener_fases`

**Situación inicial:**

El método no estaba correctamente indentado ni accedía a los atributos privados de la clase:

```python
def ejecutar_y_obtener_fases(self, prelavado, secado, encerado):
self.hacerLavado(prelavado, secado, encerado)
fases_visitadas = [self.fase]
while self.ocupado:
    self.avanzarFase()
    fases_visitadas.append(self.fase)
return fases_visitadas
```

###Solución aplicada:

Se corrigió la indentación.

Se accede a los atributos privados usando `self.__fase` y `self.__ocupado`.

```
def ejecutar_y_obtener_fases(self, prelavado, secado, encerado):
    """Ejecuta un ciclo completo y devuelve la lista de fases visitadas."""
    self.hacerLavado(prelavado, secado, encerado)
    fases_visitadas = [self.__fase]

    while self.__ocupado:
        if len(fases_visitadas) > 15:
            raise Exception("Bucle infinito detectado en la simulación de fases.")
        self.avanzarFase()
        fases_visitadas.append(self.__fase)

    return fases_visitadas
```

## Problema 2: Acceso a atributos privados

**Situación inicial:**

Los tests fallaban porque los métodos de prueba intentaban acceder a self.fase y self.ocupado directamente.

###Solución aplicada:

Se añadieron @property para exponer de manera controlada los atributos privados:

```python
@property
def fase(self):
    return self.__fase

@property
def ocupado(self):
    return self.__ocupado
```

## Problema 3: Método _cobrar

**Situación inicial:**

El cálculo de ingresos no estaba en el orden correcto y provocaba resultados inconsistentes en algunos tests.

###Solución aplicada:

Se reorganizó el orden de los cobros según las opciones seleccionadas:

```python
if self.__prelavado_a_mano:
    coste_lavado += 1.50 

if self.__secado_a_mano:
    coste_lavado += 1.00 

if self.__encerado:
    coste_lavado += 1.20
```

