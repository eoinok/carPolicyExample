#test_vehicle.py
import pytest
from CarPolicy import CarPolicy

def test_get_engine_size_cc():
    thisPolicy = CarPolicy(1234,"John Smith",1000,1500,6)
    assert thisPolicy.get_engine_size_cc() == 1500
    assert thisPolicy.get_yearly_premium() == 1000
    assert thisPolicy.get_discount() == 20
    assert thisPolicy.get_discounted_premium() == 800
    

