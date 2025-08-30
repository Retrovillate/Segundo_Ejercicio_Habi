"""
ordenar_bloques.py

Este módulo procesa un arreglo de números separados por ceros.
Cada cero marca el final de un bloque y el inicio de otro.
Los números dentro de cada bloque (rango 1-9) se ordenan de menor a mayor.
Bloques vacíos se representan con 'x', pero ceros consecutivos
se agrupan en una sola 'x'.

Ejemplo:
---------
Entrada: [1, 3, 2, 0, 7, 8, 1, 3, 0, 6, 7, 1]
Salida : "123 1378 167"

Entrada: [2, 1, 0, 0, 0, 0, 3, 4]
Salida : "12 x 34"

Entrada: [0, 1, 2, 0]
Salida : "x 12 x"
"""

from typing import List


def validar_arreglo(arreglo: List[int]) -> None:
    """
    Valida que el arreglo sea una lista de enteros entre 0 y 9.
    Lanza ValueError si no cumple.
    """
    if not isinstance(arreglo, list):
        raise ValueError("El arreglo debe ser una lista.")
    if not all(isinstance(num, int) for num in arreglo):
        raise ValueError("Todos los elementos deben ser enteros.")
    if not all(0 <= num <= 9 for num in arreglo):
        raise ValueError("Los elementos deben estar en el rango [0, 9].")


def dividir_en_bloques(arreglo: List[int]) -> List[List[int]]:
    """
    Divide el arreglo en bloques usando cero como separador.
    Ceros consecutivos generan bloques vacíos, pero luego
    se colapsan en una sola 'x' durante el procesamiento.
    """
    bloques, bloque_actual = [], []
    for numero in arreglo:
        if numero == 0:
            bloques.append(bloque_actual)
            bloque_actual = []
        else:
            bloque_actual.append(numero)
    # agregar el último bloque (aunque sea vacío)
    bloques.append(bloque_actual)
    return bloques


def ordenar_bloques(bloques: List[List[int]]) -> List[str]:
    """
    Ordena cada bloque individualmente.
    Bloques vacíos se convierten en 'x'.
    """
    resultado = []
    for bloque in bloques:
        if not bloque:
            resultado.append("x")
        else:
            resultado.append("".join(str(n) for n in sorted(bloque)))
    return resultado


def procesar_arreglo(arreglo: List[int]) -> str:
    """
    Procesa el arreglo completo:
    - Valida
    - Divide en bloques
    - Ordena cada bloque
    - Une bloques en una cadena separada por espacios.
      Si hay bloques vacíos, se imprimen como 'x', evitando duplicados.
    """
    validar_arreglo(arreglo)
    bloques = dividir_en_bloques(arreglo)
    bloques_ordenados = ordenar_bloques(bloques)

    # Si todos son 'x', devolver solo una vez
    if all(b == "x" for b in bloques_ordenados):
        return "x"

    resultado = []
    anterior_x = False
    for bloque in bloques_ordenados:
        if bloque == "x":
            if not anterior_x:
                resultado.append("x")
            anterior_x = True
        else:
            resultado.append(bloque)
            anterior_x = False

    return " ".join(resultado)


if __name__ == "__main__":
    # Ejemplo de ejecución directa
    ejemplos = [
        [1, 3, 2, 0, 7, 8, 1, 3, 0, 6, 7, 1],  # sin bloques vacíos
        [2, 1, 0, 0, 0, 0, 3, 4],              # con x intermedia
        [0, 1, 2, 0],                          # x al inicio y al final
        [0, 0, 0],                              # solo ceros -> "x"
    ]
    for arr in ejemplos:
        print(arr, "->", procesar_arreglo(arr))
