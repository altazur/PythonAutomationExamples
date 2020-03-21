from CalculatorSOAP import Calculator
import pytest

@pytest.fixture
def get_calculator():
    calculator = Calculator()
    yield calculator
