
from clases.calculadora import Calculadora
from prueba.testing import Test_calculadora

#creo la suma
#suma= Calculadora.sumar(1,2)
#print (f"la suma entre ambos numeros es {suma}")

testeando= Test_calculadora.test_suma_positiva()
print (f"su testeo es {testeando}")
