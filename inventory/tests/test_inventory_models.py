import pytest


def test_inventory_str(inventory_fixture):
    assert inventory_fixture.__str__() == str(inventory_fixture.id)
    
def test_inventory_discount_str(inventory_discount_fixture):
    assert inventory_discount_fixture.__str__() == str(inventory_discount_fixture.id)
