# tests/test_lavadero_unittest.py

import unittest
# Importamos la clase Lavadero desde el módulo padre
from lavadero import Lavadero

class TestLavadero(unittest.TestCase):
    
    # Método que se ejecuta antes de cada test.
    # Es el equivalente del @pytest.fixture en este contexto.
    def setUp(self):
        """Prepara una nueva instancia de Lavadero antes de cada prueba."""
        self.lavadero = Lavadero()

    # ----------------------------------------------------------------------    
    # Función para resetear el estado cuanto terminamos una ejecución de lavado
    # ----------------------------------------------------------------------
    def test_reseteo_estado_con_terminar(self):
        """Test: Verifica que terminar() resetea todas las flags y el estado."""
        self.lavadero.hacerLavado(True, True, True)
        self.lavadero._cobrar()
        self.lavadero.terminar()
        
        self.assertEqual(self.lavadero.fase, Lavadero.FASE_INACTIVO)
        self.assertFalse(self.lavadero.ocupado)
        self.assertFalse(self.lavadero.prelavado_a_mano)
        self.assertTrue(self.lavadero.ingresos > 0) # Los ingresos deben mantenerse
        
    # ----------------------------------------------------------------------
    # TESTS: Jerónimo
    # ----------------------------------------------------------------------    
    #---------------------------------------------------    
    # TEST 1
    #---------------------------------------------------
    def test1_estado_inicial_correcto(self):
        """
        Test 1:
        Verifica que el estado inicial es Inactivo y con 0 ingresos."""
        self.assertEqual(self.lavadero.fase, Lavadero.FASE_INACTIVO)
        self.assertEqual(self.lavadero.ingresos, 0.0)
        self.assertFalse(self.lavadero.ocupado)
        self.assertFalse(self.lavadero.prelavado_a_mano)
        self.assertFalse(self.lavadero.secado_a_mano)
        self.assertFalse(self.lavadero.encerado)

    #---------------------------------------------------
    # TEST 2
    #---------------------------------------------------
    def test2_excepcion_encerado_sin_secado(self):
        """
        Test 2: 
        Comprueba que encerar sin secado a mano lanza ValueError."""
        # _hacer_lavado: (Prelavado: False, Secado a mano: False, Encerado: True)
        with self.assertRaises(ValueError):
            self.lavadero.hacerLavado(False, False, True)

    # Desarrollo de los test
    # Jerónimo

    # --------------------------------------------------
    # TEST 3
    # --------------------------------------------------
    def test3_no_se_puede_iniciar_dos_lavados(self):
        """
        Test 3:
        Intentar iniciar un lavado cuando otro está en marcha lanza RuntimeError.
        """
        self.lavadero.hacerLavado(False, False, False)

        with self.assertRaises(RuntimeError):
            self.lavadero.hacerLavado(False, False, False)

    # --------------------------------------------------
    # TEST 4
    # --------------------------------------------------
    def test4_ingresos_prelavado(self):
        """
        Test 4:
        Lavado con prelavado a mano genera 6,50€.
        """
        self.lavadero.hacerLavado(True, False, False)
        self.lavadero.avanzarFase()  # cobra

        self.assertAlmostEqual(self.lavadero.ingresos, 6.50, places=2)

    # --------------------------------------------------
    # TEST 5
    # --------------------------------------------------
    def test5_ingresos_secado_mano(self):
        """
        Test 5:
        Lavado con secado a mano genera 6,00€.
        """
        self.lavadero.hacerLavado(False, True, False)
        self.lavadero.avanzarFase()

        self.assertAlmostEqual(self.lavadero.ingresos, 6.00, places=2)

    # --------------------------------------------------
    # TEST 6
    # --------------------------------------------------
    def test6_ingresos_secado_y_encerado(self):
        """
        Test 6:
        Lavado con secado a mano y encerado genera 7,20€.
        """
        self.lavadero.hacerLavado(False, True, True)
        self.lavadero.avanzarFase()

        self.assertAlmostEqual(self.lavadero.ingresos, 7.20, places=2)

    # --------------------------------------------------
    # TEST 7
    # --------------------------------------------------
    def test7_ingresos_prelavado_y_secado(self):
        """
        Test 7:
        Lavado con prelavado y secado a mano genera 7,50€.
        """
        self.lavadero.hacerLavado(True, True, False)
        self.lavadero.avanzarFase()

        self.assertAlmostEqual(self.lavadero.ingresos, 7.50, places=2)

    # --------------------------------------------------
    # TEST 8
    # --------------------------------------------------
    def test8_ingresos_completo(self):
        """
        Test 8:
        Lavado con prelavado, secado a mano y encerado genera 8,70€.
        """
        self.lavadero.hacerLavado(True, True, True)
        self.lavadero.avanzarFase()

        self.assertAlmostEqual(self.lavadero.ingresos, 8.70, places=2)

    # --------------------------------------------------
    # TEST 9: Flujo rápido sin extras
    # --------------------------------------------------
    def test9_flujo_rapido_sin_extras(self):
        """
        Test 9: 
        Simula el flujo rápido sin opciones opcionales."""
        fases_esperadas = [0, 1, 3, 4, 5, 6, 0]
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(prelavado=False, secado=False, encerado=False)
        self.assertEqual(fases_obtenidas, fases_esperadas,
                        f"Secuencia de fases incorrecta.\nEsperadas: {fases_esperadas}\nObtenidas: {fases_obtenidas}")


    # --------------------------------------------------
    # TEST 10: Flujo con prelavado
    # --------------------------------------------------
    def test10_flujo_con_prelavado(self):
        """
        Test 10:
        Flujo con prelavado a mano."""
        fases_esperadas = [0, 1, 2, 3, 4, 5, 6, 0]
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(prelavado=True, secado=False, encerado=False)
        self.assertEqual(fases_obtenidas, fases_esperadas,
                        f"Secuencia de fases con prelavado incorrecta.\nEsperadas: {fases_esperadas}\nObtenidas: {fases_obtenidas}")

    # --------------------------------------------------
    # TEST 11: Flujo con secado a mano
    # --------------------------------------------------
    def test11_flujo_con_secado_mano(self):
        """
        Test 11:
        Flujo con secado a mano sin prelavado."""
        fases_esperadas = [0, 1, 3, 4, 5, 7, 0]
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(prelavado=False, secado=True, encerado=False)
        self.assertEqual(fases_obtenidas, fases_esperadas,
                     f"Secuencia de fases con secado a mano incorrecta.\nEsperadas: {fases_esperadas}\nObtenidas: {fases_obtenidas}")

    # --------------------------------------------------
    # TEST 12: Flujo completo
    # --------------------------------------------------
    def test12_flujo_completo(self):
        """
        Test 12:
        Flujo completo con todas las opciones."""
        fases_esperadas = [0, 1, 2, 3, 4, 5, 7, 8, 0]
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(prelavado=True, secado=True, encerado=True)
        self.assertEqual(fases_obtenidas, fases_esperadas,
                     f"Secuencia de fases completa incorrecta.\nEsperadas: {fases_esperadas}\nObtenidas: {fases_obtenidas}")
          
    # --------------------------------------------------
    # TEST 13: Flujo prelavado y secado
    # --------------------------------------------------  
    def test13_flujo_prelavado_y_secado(self):
        """
        Test 13:
        Flujo con prelavado y secado a mano, sin encerado."""
        fases_esperadas = [0, 1, 2, 3, 4, 5, 7, 0]
        
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(prelavado=True, secado=True, encerado=False)
        
        self.assertEqual(fases_obtenidas, fases_esperadas,
                        f"Secuencia de fases incorrecta con prelavado y secado a mano.\nEsperadas: {fases_esperadas}\nObtenidas: {fases_obtenidas}")

    # --------------------------------------------------
    # TEST 14: Flujo completo finalización
    # --------------------------------------------------
    def test14_flujo_completo_finalizacion(self):
        """
        Test 14:
        Flujo completo con todas las opciones y finalización correcta."""
        fases_esperadas = [0, 1, 2, 3, 4, 5, 7, 8, 0]
        
        fases_obtenidas = self.lavadero.ejecutar_y_obtener_fases(prelavado=True, secado=True, encerado=True)
        
        self.assertEqual(fases_obtenidas, fases_esperadas,
                        f"Secuencia de fases incorrecta en flujo completo con encerado.\nEsperadas: {fases_esperadas}\nObtenidas: {fases_obtenidas}")
    
# Bloque de ejecución para ejecutar los tests si el archivo es corrido directamente
if __name__ == '__main__':
    unittest.main()