import unittest
from StringCalculator import StringCalculator


class Test(unittest.TestCase):
    
    __stringCalculator = StringCalculator()

    def testAddEmpty(self):
        self.assertEquals(self.__stringCalculator.add(""), 0, "Se ha intentado sumar vacio, y no ha dado 0")
        
    def testAddSingleNumber(self):
        self.assertEquals(self.__stringCalculator.add("1"), 1, "Se ha intentado sumar 1+vacio (un numero) y no ha dado 1")
        
    def testAddOtherSingleNumber(self):
        self.assertEquals(self.__stringCalculator.add("2"), 2, "Se ha intentado sumar 2+vacio (un numero) y no ha dado 2")   
    
    def testAddTwoNumbers(self):
        self.assertEquals(self.__stringCalculator.add("1,2"), 3, "Se ha intentado sumar 1+2 (dos numeros) y no ha dado 3")  
    
    def testAddMoreThanTwoNumbers(self):
        self.assertEquals(self.__stringCalculator.add("1,2,3,4,5"), 15, "Se ha intentado sumar 1+2+3+4+5 (mas de dos numeros) y no ha dado 15") 
        
    def testAddTwoNumbersWithBreakLine(self):
        self.assertEquals(self.__stringCalculator.add("1\n2"), 3, "Se ha intentado sumar 1+2 con el delimitador de salto de linea y no ha dado 3")

    def testAddNumbersWithBreakLineAndComma(self):
        self.assertEquals(self.__stringCalculator.add("1\n2,3"), 6, "Se ha intentado sumar 1+2+3 con el delimitador de salto de linea y la coma y no ha dado 6")
    
    def testAddNumbersWithSpecifiedDelimiter(self):
        self.assertEquals(self.__stringCalculator.add("//;\n1;2"), 3, "Se ha intentado sumar 1+2 con el delimitador especificado (;) y no ha dado 3")  
        
    def testAddNegativeNumber(self):
        try:
            self.__stringCalculator.add("-1")
            self.fail("Se ha intentado sumar -1+vacio y no se ha devuelto ninguna excepcion")
        except Exception as exc:
            self.assertEquals(exc.message, "Negatives not allowed -1", "Se ha intentado sumar -1+vacio y no ha devuelvo una excepcion con el texto \"negatives not allowed -1\"")
    
    def testAddMultipleNegativeNumber(self):
        try:
            self.__stringCalculator.add("-1,-2")
            self.fail("Se ha intentado sumar -1+-2+vacio y no se ha devuelto ninguna excepcion")
        except Exception as exc:
            self.assertEquals(exc.message, "Negatives not allowed -1,-2", "Se ha intentado sumar -1+-2+vacio y no ha devuelvo una excepcion con el texto \"negatives not allowed -1\"")
    
    def testAddNumbersBiggerThanThousand(self):
        self.assertEquals(self.__stringCalculator.add("1,1005"), 1, "Se ha intentado sumar 1+1005 (1 + un numero mayor que 1000) y no ha dado 1")  

if __name__ == "__main__":
    unittest.main()