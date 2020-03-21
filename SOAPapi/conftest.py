from CalculatorSOAP import Calculator
import pytest

@pytest.fixture
def get_calculator():
    calculator = Calculator()
    yield calculator

def pytest_addoption(parser):
    parser.addoption('--SOAPver', default='1', help='SOAP version: 1 or 2')

@pytest.fixture
def soap_version(request):
    return request.config.getoption('--SOAPver')
