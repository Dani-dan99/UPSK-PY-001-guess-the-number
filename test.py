import unittest
from main import guessTheNumber, guess, playerTurn;
from unittest.mock import patch
from io import StringIO #ste módulo proporciona herramientas para trabajar con flujos de entrada y salida de datos y StringIO es una clase que te permite trabajar con cadenas como si fueran archivos de texto.



class TestGuessTheNumber(unittest.TestCase): #El código define una clase de prueba TestGuessTheNumber que hereda de unittest.TestCase
    def test_guessTheNumber(self):
        for _ in range(100): # Ejecuta la función varias veces para asegurarse de que siempre devuelve un número dentro del rango esperado
            number = guessTheNumber()
            self.assertTrue(1 <= number <= 100, f"El número {number} está fuera del rango esperado")

class TestGuessFunction(unittest.TestCase):
    def test_guess(self):
        # Adivinando el número correcto
        result, correct = guess(50, 50)
        self.assertEqual(result, '¡Yay! Es el número, lograste adivinarlo') #Método de aserción assertEqual() y assertTrue()/assertFalse() para verificar si los resultados son los esperados y si la corrección es verdadera o falsa.
        self.assertTrue(correct)

        # Número más alto 
        result, correct = guess(75, 50)
        self.assertEqual(result, 'El número ingresado es más alto de lo esperado, prueba de nuevo')
        self.assertFalse(correct)

        # Número más bajo 
        result, correct = guess(25, 50)
        self.assertEqual(result, 'El número ingresado es más bajo de lo esperado, prueba de nuevo')
        self.assertFalse(correct)


class TestPlayerTurnFunction(unittest.TestCase):
    @patch('builtins.input', side_effect=['abc', '50'])
    def test_playerTurn(self, mock_input):
        captured_output = StringIO()  # Salida para verificar los mensajes de error
        import sys
        sys.stdout = captured_output

        # Primer intento
        result = playerTurn()
        self.assertEqual(result, 50)  # Debería devolver el número ingresado (correctamente)
        self.assertEqual(captured_output.getvalue().strip(), "Por favor, ingresa un número válido.")





if __name__ == '__main__':
    unittest.main()




