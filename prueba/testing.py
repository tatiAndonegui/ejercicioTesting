import unittest 
from clases.calculadora import Calculadora

class  Test_calculadora (unittest.TestCase):

    def test_suma_positiva(self):
        self.assertEqual(Calculadora.sumar(2,3),5) 
