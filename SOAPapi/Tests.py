import pytest

def test_soap_calc_add(get_calculator):
   assert get_calculator.add(1,5) == 6
