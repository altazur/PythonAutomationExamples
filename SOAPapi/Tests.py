import pytest

def test_soap_calc_add(get_calculator, soap_version):
   assert get_calculator.add(1,5, soap_version) == 6
