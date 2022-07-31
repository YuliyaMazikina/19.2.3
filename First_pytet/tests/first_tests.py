import pytest
from app.calculator import Calculator


class TestCalc: # название класса тестов
    def setup(self): # Предварительный метод setup в котором мы подключаем тестируемый объект Калькулятор
        self.calc = Calculator

    def test_multiply_calculate_correctly(self): # простой тест на проверку правильности умножения
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_calculate_correctly(self): # простой тест на проверку правильности деления
        assert self.calc.division(self, 8, 2) == 4

    def test_subtraction_calculate_correctly(self): # простой тест на проверку правильности вычетание
        assert self.calc.subtraction(self, 8, 4) == 4

    def test_adding_calculate_correctly(self): # простой тест на проверку правильности сложение
        assert self.calc.adding(self, 2, 2) == 4
