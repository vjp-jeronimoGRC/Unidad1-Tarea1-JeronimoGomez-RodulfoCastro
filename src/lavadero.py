# lavadero.py

# Simula el estado y las operaciones de un túnel de lavado de coches.
# Cumple con los requisitos de estado, avance de fase y reglas de negocio.

class Lavadero:

    FASE_INACTIVO = 0
    FASE_COBRANDO = 1
    FASE_PRELAVADO_MANO = 2
    FASE_ECHANDO_AGUA = 3
    FASE_ENJABONANDO = 4
    FASE_RODILLOS = 5
    FASE_SECADO_AUTOMATICO = 6
    FASE_SECADO_MANO = 7
    FASE_ENCERADO = 8

    #Constructor de la clase. Inicializa el lavadero

    def __init__(self):        
        self.__ingresos = 0.0
        self.__fase = self.FASE_INACTIVO
        self.__ocupado = False
        self.__prelavado_a_mano = False
        self.__secado_a_mano = False
        self.__encerado = False
        self.terminar() 


    #  Propiedades de solo lectura de la clase Lavadero.
    #  Estas propiedades permiten consultar el estado interno del lavadero (fase actual, ingresos acumulados, estado de ocupación y servicios adicionales seleccionados) sin acceder directamente a los atributos privados, respetando el principio de encapsulación.

    @property
    def fase(self):
        return self.__fase

    @property
    def ingresos(self):
        return self.__ingresos

    @property
    def ocupado(self):
        return self.__ocupado
    
    @property
    def prelavado_a_mano(self):
        return self.__prelavado_a_mano

    @property
    def secado_a_mano(self):
        return self.__secado_a_mano

    @property
    def encerado(self):
        return self.__encerado

    # Finaliza el ciclo de lavado y restablece el estado interno del lavadero.
    # Este método devuelve el lavadero a su estado inicial, marcándolo como inactivo y liberándolo para un nuevo servicio, 
    # además de limpiar todas las opciones de lavado seleccionadas.

    def terminar(self):
        self.__fase = self.FASE_INACTIVO
        self.__ocupado = False
        self.__prelavado_a_mano = False
        self.__secado_a_mano = False
        self.__encerado = False

    # Inicia un nuevo ciclo de lavado, validando reglas de negocio.
        
    # :raises RuntimeError: Si el lavadero está ocupado (Requisito 3).
    # :raises ValueError: Si se intenta encerar sin secado a mano (Requisito 2).

    def hacerLavado(self, prelavado_a_mano, secado_a_mano, encerado):
        
        if self.__ocupado:
            raise RuntimeError("No se puede iniciar un nuevo lavado mientras el lavadero está ocupado")
        
        if not secado_a_mano and encerado:
            raise ValueError("No se puede encerar el coche sin secado a mano")
        
        self.__fase = self.FASE_INACTIVO  
        self.__ocupado = True
        self.__prelavado_a_mano = prelavado_a_mano
        self.__secado_a_mano = secado_a_mano
        self.__encerado = encerado
        
    # Calcula y añade los ingresos según las opciones seleccionadas (Requisitos 4-8).
    # Precio base: 5.00€ (Implícito, 5.00€ de base + 1.50€ de prelavado + 1.00€ de secado + 1.20€ de encerado = 8.70€)

    def _cobrar(self):
        coste_lavado = 5.00
        
        # A este bloque de condiciones se le ha modificado los valores que se le añaden al coste_lavado
        if self.__prelavado_a_mano:
            coste_lavado += 1.50 
        
        if self.__secado_a_mano:
            coste_lavado += 1.00 
            
        if self.__encerado:
            coste_lavado += 1.20 
            
        self.__ingresos += coste_lavado
        return coste_lavado


    # Gestiona la transición entre las distintas fases del túnel de lavado.

    # El método avanza el estado interno del lavadero en función de la fase actual y de las opciones 
    # seleccionadas por el usuario (prelavado a mano, secado a mano y encerado).

    # Durante el desarrollo se corrigió la lógica de transición desde la fase de rodillos, 
    # añadiendo condiciones para contemplar correctamente los flujos con secado manual y encerado, 
    # evitando saltos incorrectos de fase y garantizando la finalización correcta del ciclo.

    def avanzarFase(self):
       
        if not self.__ocupado:
            return

        if self.__fase == self.FASE_INACTIVO:
            coste_cobrado = self._cobrar()
            self.__fase = self.FASE_COBRANDO
            print(f" (COBRADO: {coste_cobrado:.2f} €) ", end="")

        elif self.__fase == self.FASE_COBRANDO:
            if self.__prelavado_a_mano:
                self.__fase = self.FASE_PRELAVADO_MANO
            else:
                self.__fase = self.FASE_ECHANDO_AGUA 
        
        elif self.__fase == self.FASE_PRELAVADO_MANO:
            self.__fase = self.FASE_ECHANDO_AGUA
        
        elif self.__fase == self.FASE_ECHANDO_AGUA:
            self.__fase = self.FASE_ENJABONANDO

        elif self.__fase == self.FASE_ENJABONANDO:
            self.__fase = self.FASE_RODILLOS
        
        #A este bloque de condiciones se le han añadido los bloques de if ... else ... de __secado_a_mano y __encerado  
        elif self.__fase == self.FASE_RODILLOS:
            if self.__secado_a_mano:
                self.__fase = self.FASE_SECADO_MANO

            else:
                self.__fase = self.FASE_SECADO_AUTOMATICO
        
        elif self.__fase == self.FASE_SECADO_AUTOMATICO:
            self.terminar()
        
        elif self.__fase == self.FASE_SECADO_MANO:
            if self.__encerado:
                self.__fase = self.FASE_ENCERADO
            else:
                self.terminar()

        elif self.__fase == self.FASE_ENCERADO:
            self.terminar()

        else:
            raise RuntimeError(f"Estado no válido: Fase {self.__fase}. El lavadero va a estallar...")

    # Muestra en pantalla la descripción de la fase actual del lavadero.

    # Se utiliza un diccionario fases_map que relaciona los códigos internos de fase con su descripción en texto legible. 
    # En caso de que la fase no coincida con ninguna definida, se imprime un mensaje indicando un estado no válido

    def imprimir_fase(self):
        fases_map = {
            self.FASE_INACTIVO: "0 - Inactivo",
            self.FASE_COBRANDO: "1 - Cobrando",
            self.FASE_PRELAVADO_MANO: "2 - Haciendo prelavado a mano",
            self.FASE_ECHANDO_AGUA: "3 - Echándole agua",
            self.FASE_ENJABONANDO: "4 - Enjabonando",
            self.FASE_RODILLOS: "5 - Pasando rodillos",
            self.FASE_SECADO_AUTOMATICO: "6 - Haciendo secado automático",
            self.FASE_SECADO_MANO: "7 - Haciendo secado a mano",
            self.FASE_ENCERADO: "8 - Encerando a mano",
        }
        print(fases_map.get(self.__fase, f"{self.__fase} - En estado no válido"), end="")

    # Muestra en pantalla el estado completo del lavadero.

    # Se incluyen:

    #    Ingresos acumulados
    #    Estado de ocupado/no ocupado
    #    Opciones activas (prelavado, secado a mano, encerado)
    #    Fase actual (usando imprimir_fase())

    # Permite tener una visión rápida de todo el estado interno del lavadero.

    def imprimir_estado(self):
        print("----------------------------------------")
        print(f"Ingresos Acumulados: {self.ingresos:.2f} €")
        print(f"Ocupado: {self.ocupado}")
        print(f"Prelavado a mano: {self.prelavado_a_mano}")
        print(f"Secado a mano: {self.secado_a_mano}")
        print(f"Encerado: {self.encerado}")
        print("Fase: ", end="")
        self.imprimir_fase()
        print("\n----------------------------------------")
        
    # Esta función es útil para pruebas unitarias, no es parte del lavadero real
    # nos crea un array con las fases visitadas en un ciclo completo
    
    # A este método se le ha añadido una tabulación  
    def ejecutar_y_obtener_fases(self, prelavado, secado, encerado):
        """Ejecuta un ciclo completo y devuelve la lista de fases visitadas."""
        self.hacerLavado(prelavado, secado, encerado)
        fases_visitadas = [self.__fase]

        while self.__ocupado:
            # Usamos un límite de pasos para evitar bucles infinitos en caso de error
            if len(fases_visitadas) > 15:
                raise Exception("Bucle infinito detectado en la simulación de fases.")
            self.avanzarFase()
            fases_visitadas.append(self.__fase)

        return fases_visitadas
