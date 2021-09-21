import pytest


def test_order_str(order_fixture):
    assert order_fixture.__str__() == str(order_fixture.created)

def test_order_item_str(order_item_fixture):
    assert order_item_fixture.__str__() == str(order_item_fixture.id)
