# Programa que solicita la quintupla de un AFD o AFN para crearlo y después verificar cadenas que son aceptadas o rechazadas.

class Automata: # Definición de la Clase Automata para representar un AFD o un AFN.
    def __init__(self, estados, alfabeto, transiciones, estado_inicial, estados_aceptacion, es_determinista=True): # Inicialización del autómata con su quintupla y un estado para saber si es un AFD o un AFN
        # self se utiliza para las instancias de una clase y poder acceder a sus atributos, variables y metodos.
        self.estados = estados  # Lista de estados.
        self.alfabeto = alfabeto  # Lista de símbolos del alfabeto.
        self.transiciones = transiciones  # Tabla de transiciones.
        self.estado_inicial = estado_inicial  # Estado inicial.
        self.estados_aceptacion = estados_aceptacion  # Lista de estados de aceptación.
        self.es_determinista = es_determinista  # Indica si es un AFD (True) o un AFN (False).

    def verificar_cadena(self, cadena): # Función para elegir el método para verificar una cadena para un AFD o AFN.
        if self.es_determinista:
            return self.verificar_cadena_afd(cadena)  # Llama al método de verificación para AFD.
        else:
            return self.verificar_cadena_afn(cadena)  # Llama al método de verificación para AFN.

    def verificar_cadena_afd(self, cadena): # Funcion para verificar una cadena de un AFD.
        estado_actual = self.estado_inicial  # Inicia en el estado inicial.
        for simbolo in cadena:  # Recorre cada símbolo de la cadena.
            if simbolo not in self.alfabeto:  # Si el símbolo no pertenece al alfabeto, la cadena no es válida.
                print(f"Símbolo '{simbolo}' no pertenece al alfabeto.")
                return False
            estado_actual = self.transiciones.get((estado_actual, simbolo))  # Busca la transición.
            if estado_actual is None:  # Si no hay transición, la cadena no es aceptada.
                print("Transición no definida. La cadena no es aceptada.")
                return False
        # Retorna True si el estado final está en los estados de aceptación.
        return estado_actual in self.estados_aceptacion

    def verificar_cadena_afn(self, cadena): # Función para verificar una cadena de un AFN.
        estados_actuales = {self.estado_inicial}  # Conjunto de estados iniciales.
        for simbolo in cadena:  # Recorre cada símbolo de la cadena.
            if simbolo not in self.alfabeto:  # Si el símbolo no pertenece al alfabeto, la cadena no es válida.
                print(f"Símbolo '{simbolo}' no pertenece al alfabeto.")
                return False
            nuevos_estados = set()  # Conjunto para los nuevos estados alcanzables.
            for estado in estados_actuales:  # Para cada estado actual, busca transiciones.
                if (estado, simbolo) in self.transiciones:
                    nuevos_estados.update(self.transiciones[(estado, simbolo)])  # Agrega estados destino.
            estados_actuales = nuevos_estados  # Actualiza los estados actuales.
            if not estados_actuales:  # Si no hay estados alcanzables, la cadena no es aceptada.
                return False
        # Retorna True si al menos uno de los estados actuales es de aceptación.
        return any(estado in self.estados_aceptacion for estado in estados_actuales)


def generar_tabla_transiciones(estados, alfabeto, es_determinista): # Función para generar dinámicamente la tabla de transiciones para AFD o AFN.
    print("\nTabla de transiciones:")
    transiciones = {}  # Diccionario para almacenar las transiciones, para guardar el estado y el elemento del alfabeto.

    for estado in estados:  # Itera por cada estado.
        for simbolo in alfabeto:  # Itera por cada símbolo del alfabeto.
            if es_determinista:
                # En un AFD, cada transición lleva a un único estado.
                destino = input(f"Transición ({estado}, {simbolo}): ")
                if destino.strip():  # Si el usuario ingresó algo, agrega la transición.
                    transiciones[(estado, simbolo)] = destino.strip()
            else:
                # En un AFN, una transición puede llevar a múltiples estados.
                destino = input(f"Transición ({estado}, {simbolo}) [separa múltiples estados con comas]: ")
                if destino.strip():  # Divide en una lista los múltiples estados destino.
                    transiciones[(estado, simbolo)] = destino.strip().split(',')
    return transiciones


def definir_automata(es_determinista): # Define al autómata ingresando los elementos de la quíntupla.
    tipo = "AFD" if es_determinista else "AFN" # Comprobamos si la variable es_determinista esta en TRUE (AFD) o FALSE (AFN). Operador terneario.
    print(f"\nIntroduce la quíntupla del {tipo}:") # Imprime el tipo de autómata que se va a realizar, f es para escribir texto y variables.
    estados = input("  Conjunto de estados (separados por comas): ").split(',') # Dividimos la cadena hasta que encontremos el símbolo de la coma.
    alfabeto = input("  Alfabeto (separado por comas): ").split(',')

    # Genera la tabla de transiciones de forma dinámica.
    transiciones = generar_tabla_transiciones(estados, alfabeto, es_determinista)

    estado_inicial = input("\n  Estado inicial: ").strip()
    estados_aceptacion = input("  Estados de aceptación (separados por comas): ").split(',')
    print("\nAutómata creado con éxito...")
    # Retorna el autómata creado con la quíntupla completa.
    return Automata(estados, alfabeto, transiciones, estado_inicial, estados_aceptacion, es_determinista)


def main(): # Función principal del programa. Contiene el menú y la interacción con el usuario.
    print("----------------Autómatas Finitos Deterministas y No Deterministas----------------")
    while True:
        print("\nOpciones:")
        print("1. Autómata Finito Determinista (AFD)")
        print("2. Autómata Finito No Determinista (AFN)")
        print("3. Salir")
        opcion = input("Selecciona una opción: ").strip() # strip elimina el espacio inicial y final en caso de existir.

        if opcion == '1':
            automata = definir_automata(es_determinista=True)  # Define un AFD.
        elif opcion == '2':
            automata = definir_automata(es_determinista=False)  # Define un AFN.
        elif opcion == '3':
            print("\nSaliendo del programa...")
            return  # Sale del programa.
        else:
            print("Opción inválida. Intenta de nuevo.")
            continue

        while True:
            print("\nOpciones:")
            print("1. Verificar una cadena")
            print("2. Ingresar un autómata nuevo")
            print("3. Regresar al menú principal")
            subopcion = input("Selecciona una opción: ").strip()
            if subopcion == '1':
                cadena = input("\nIngresa la cadena a verificar: ").strip()
                if automata.verificar_cadena(cadena):  # Verifica si la cadena es aceptada.
                    print(" Cadena aceptada.")
                else:
                    print(" Cadena no aceptada.")
            elif subopcion == '2':  # Permite cambiar el autómata.
                break
            elif subopcion == '3':  # Regresa al menú principal.
                print("\nRegresando al menú principal...")
                return
            else:
                print("\nOpción inválida. Intenta de nuevo.")


if __name__ == "__main__":
    main()  # Ejecuta el programa principal.