# Pruebas Unitarias

En esta sección se documentan las pruebas realizadas sobre la clase `Lavadero` y sus métodos.

## Objetivo

Verificar que la clase `Lavadero` cumple con los requisitos de negocio:

- Estados y transiciones de fases correctas.
- Cálculo de ingresos según opciones seleccionadas.
- Prevención de errores (encerar sin secado, iniciar lavado cuando el lavadero está ocupado, etc.).

## Conjunto de pruebas

Se utilizaron tests unitarios con `unittest`. El comando para ejecutar todos los tests:

```bash
PYTHONPATH=src python3 test/test_lavadero_unittest.py -v
```

## Ejemplos de test dados en un principio

1. Estado inicial correcto

```python
def test1_estado_inicial_correcto(self):
    self.assertFalse(self.lavadero.ocupado)
    self.assertEqual(self.lavadero.fase, self.lavadero.FASE_INACTIVO)
    self.assertEqual(self.lavadero.ingresos, 0)
```

2. Excepción al intentar encerar sin secado

```python
def test2_excepcion_encerado_sin_secado(self):
    with self.assertRaises(ValueError):
        self.lavadero.hacerLavado(prelavado_a_mano=False, secado_a_mano=False, encerado=True)
```

A partir de hay se empieza a crear el resto de tests unitarios.

## Explicación breve de los test

- **test1_estado_inicial_correcto:** Verifica que el lavadero inicia en estado Inactivo con ingresos 0.

- **test2_excepcion_encerado_sin_secado:** Comprueba que encerar sin secado a mano lanza `ValueError`.

- **test3_no_se_puede_iniciar_dos_lavados:** Evita iniciar un lavado si el lavadero ya está ocupado (`RuntimeError`).

- **test4 a test8:** Comprueban el cálculo de ingresos según las opciones seleccionadas (prelavado, secado, encerado).

- **test9 a test14:** Simulan los flujos completos del lavado, incluyendo combinaciones de prelavado, secado a mano y encerado.

- **test_reseteo_estado_con_terminar:** Verifica que `terminar()` restablece todas las flags y el estado del lavadero.
