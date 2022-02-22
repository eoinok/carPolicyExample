#test_vehicle.py
import pytest
from Policy import Policy

def test_str():
    thisPolicy = Policy("1234", "John Smith", 2500)
    assert thisPolicy.__str__() == "1234: John Smith"

def test_yearly_premium():
    thisPolicy = Policy("1234", "John Smith", 2500)
    assert thisPolicy.get_yearly_premium() == 2500
    

