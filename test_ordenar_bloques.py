import unittest
from ordernar_bloques import procesar_arreglo


class TestProcesarArreglo(unittest.TestCase):
    def test_arreglo_normal(self):
        ejemplo = [1, 3, 2, 0, 7, 8, 1, 3, 0, 6, 7, 1]
        resultado = procesar_arreglo(ejemplo)
        self.assertEqual(resultado, "123 1378 167")

    def test_ceros_consecutivos(self):
        ejemplo = [2, 1, 0, 0, 0, 0, 3, 4]
        resultado = procesar_arreglo(ejemplo)
        self.assertEqual(resultado, "12 x 34")

    def test_solo_un_bloque(self):
        ejemplo = [9, 1, 5]
        resultado = procesar_arreglo(ejemplo)
        self.assertEqual(resultado, "159")

    def test_todos_ceros(self):
        ejemplo = [0, 0, 0]
        resultado = procesar_arreglo(ejemplo)
        # Solo debe devolver "x" porque todos son ceros → un único bloque vacío
        self.assertEqual(resultado, "x")

    def test_bloques_vacios_en_medio(self):
        ejemplo = [4, 0, 0, 5]
        resultado = procesar_arreglo(ejemplo)
        self.assertEqual(resultado, "4 x 5")

    def test_valores_invalidos_tipo(self):
        ejemplo = [1, "2", 3]  # Contiene string
        with self.assertRaises(ValueError):
            procesar_arreglo(ejemplo)

    def test_valores_invalidos_fuera_rango(self):
        ejemplo = [1, 10, 3]  # 10 está fuera de rango
        with self.assertRaises(ValueError):
            procesar_arreglo(ejemplo)

    def test_lista_vacia(self):
        ejemplo = []
        resultado = procesar_arreglo(ejemplo)
        # Un único bloque vacío
        self.assertEqual(resultado, "x")

    def test_ceros_intercalados(self):
        ejemplo = [0, 1, 2, 0]
        resultado = procesar_arreglo(ejemplo)
        self.assertEqual(resultado, "x 12 x")


if __name__ == '__main__':
    unittest.main()
