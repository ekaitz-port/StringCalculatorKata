import re

class StringCalculator(object):
    
    __REGULAR_EXPRESION_TO_SPLIT = r'[,\n]\s*'
    __DELIMITER_INDICATOR = "//"
    __BREAK_LINE = "\n"
    __DELIMITER_POSITION = 2
    __ERROR_MESSAGE = "Negatives not allowed "
    __NEGATIVE = "-"
    
    def __init__(self):
        '''
        Constructor
        '''
    
    def add(self, numbers):
        if len(numbers) == 0: return 0
        
        arr_numbers = self.__convertToNumberArray(numbers)  
        self.__checkHasNegatives(numbers)
        arr_numbers = self.__removeNumbersMajorThan1000(arr_numbers)
        
        return sum(arr_numbers)
    
    def __checkHasNegatives(self, numbers):
        if self.__NEGATIVE in numbers:
            error = self.__ERROR_MESSAGE + numbers
            raise Exception(error)
    
    def __convertToNumberArray(self, numbers):
        if self.__DELIMITER_INDICATOR in numbers:
            delimiter = numbers[self.__DELIMITER_POSITION]
            numbers = numbers[numbers.find(self.__BREAK_LINE)+1:]
        else: 
            delimiter = self.__REGULAR_EXPRESION_TO_SPLIT
        splittedNumbers = [int(number) for number in self.__splitBy(numbers, delimiter)]
        
        return splittedNumbers

    def __splitBy(self, array, splitExpression):
        return re.split(splitExpression, array)
    
    def __removeNumbersMajorThan1000(self, array):
        newArray = [number for number in array if self.__isNotMajorThan1000(number)]
        
        return newArray
    
    def __isNotMajorThan1000(self, number):
        return number <= 1000