# Proyecto: Ordenar bloques de números 

Este proyecto procesa un arreglo de enteros (1 a 9) separados por ceros,
ordenando cada bloque y devolviendo la secuencia ordenada.  
Los bloques vacíos (uno o más ceros consecutivos) se representan con `X`.

---

## Tecnologías utilizadas
- **Python 3.10+** (o cualquier versión moderna de Python 3)
- **unittest** ( pruebas incluido por defecto en Python)
- **Guía de estilos PEP8** para mantener el código legible
- **Test-Driven Development (TDD)** como metodología principal

## Enfoque de desarrollo
1. **Escribimos primero las pruebas unitarias** para cada caso esperado.
2. **Ejecutamos las pruebas (fallan)** porque el código aún no está implementado.
3. **Implementamos la lógica mínima necesaria** para que pase cada prueba.
4. **Refactorizamos el código** manteniendo todos los tests en verde.

---

## Estructura del proyecto

Segundo_Ejercicio_Habi/
│
├── ordenar_bloques.py       # Código principal con la función
├── test_ordenar_bloques.py  # Pruebas unitarias
├── README.md

---

## Reglas de procesamiento
1. Los ceros actúan como separadores de bloques.
2. Si un bloque está vacío (dos ceros consecutivos o cero al inicio/final), se coloca `"x"`.
3. Los números de cada bloque se concatenan sin separadores internos.
4. Los bloques resultantes se separan por un espacio.

### Ejemplos
- Entrada: `[1, 2, 3, 0, 1, 3, 7, 8, 0, 1, 6, 7]` → Salida: `"123 1378 167"`  
- Entrada: `[1, 2, 0, 1, 5, 0, 3, 4]` → Salida: `"12 15 34"`  
- Entrada: `[0, 1, 2, 0]` → Salida: `"x 12 x"`  

---

## Archivos principales
- `ordenar_bloques.py` → Contiene la función principal `procesar_arreglo(arreglo)`.
- `test_ordenar_bloques.py` → Contiene pruebas unitarias con `unittest`.

---

## Ejecución
Para ejecutar el script:
```bash
python ordenar_bloques.py
```

---

## Ejecución de pruebas
Para correr las pruebas unitarias:
```bash
python -m unittest test_ordenar_bloques.py
```

---

## Guía de nombres de tests y cobertura

Los nombres de los tests siguen el patrón **`test_<que_valida>`**, para facilitar lectura y mantenimiento:

- **`test_arreglo_normal`**  
  Valida un caso sin bloques vacíos intermedios; solo ceros simples que separan bloques con números.  
  - Entrada: `[1, 3, 2, 0, 7, 8, 1, 3, 0, 6, 7, 1]` → Salida: `"123 1378 167"`

- **`test_ceros_consecutivos`**  
  Verifica que ceros consecutivos generen **una sola** `x` en la salida.  
  - Entrada: `[2, 1, 0, 0, 0, 0, 3, 4]` → Salida: `"12 x 34"`

- **`test_solo_un_bloque`**  
  Caso con un único bloque sin ceros.  
  - Entrada: `[9, 1, 5]` → Salida: `"159"`

- **`test_todos_ceros`**  
  Verifica que múltiples ceros se colapsen a **una sola** `x`.  
  - Entrada: `[0, 0, 0]` → Salida: `"x"`

- **`test_bloques_vacios_en_medio`**  
  Caso con ceros consecutivos en medio.  
  - Entrada: `[4, 0, 0, 5]` → Salida: `"4 x 5"`

- **`test_bloques_con_ceros_en_extremos`**  
  Valida ceros al **inicio y al final**.  
  - Entrada: `[0, 1, 2, 0]` → Salida: `"x 12 x"`

- **`test_valores_invalidos_tipo`**  
  Rechaza elementos **no enteros** con `ValueError`.  
  - Entrada: `[1, "2", 3]`

- **`test_valores_invalidos_fuera_rango`**  
  Rechaza enteros **fuera de `[0, 9]`** con `ValueError`.  
  - Entrada: `[1, 10, 3]`

- **`test_lista_vacia`**  
  Lista sin elementos se considera un único bloque vacío.  
  - Entrada: `[]` → Salida: `"x"`

> **Cobertura funcional:** con estos tests se cubren rutas felices, ceros consecutivos, ceros en extremos, valores inválidos por tipo y por rango, y arreglo vacío.

---

## Autor
**Msc. Inteligencia Artificial Cristian David Villate Martínez**
