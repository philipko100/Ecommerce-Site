import pytest


def test_customer_str(customer_fixture):
    assert customer_fixture.__str__() == "user1"

def test_customer_str_admin(adminuser_fixture):
    assert adminuser_fixture.__str__() == "admin_user"

def test_customer_email_no_input(customer_factory):
    with pytest.raises(ValueError) as e:
        test = customer_factory.create(email="")
    assert str(e.value) == "You must provide an email address"
    