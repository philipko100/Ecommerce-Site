import pytest


def test_customer_str(customer_fixture):
    assert customer_fixture.__str__() == "user1"

def test_customer_str_admin(adminuser_fixture):
    assert adminuser_fixture.__str__() == "admin_user"

def test_customer_email_no_input(customer_factory):
    with pytest.raises(ValueError) as e:
        test = customer_factory.create(email="")
    assert str(e.value) == "Customer Account: You must provide an email address"
    
def test_customer_email_no_incorrect(customer_factory):
    with pytest.raises(ValueError) as e:
        test = customer_factory.create(email="a.com")
    assert str(e.value) == "You must provide a valid email address"

def test_admin_email_no_input(customer_factory):
    with pytest.raises(ValueError) as e:
        test = customer_factory.create(email="", is_staff=True, is_superuser=True)
    assert str(e.value) == "Superuser Account: You must provide an email address"
    
def test_admin_email_no_incorrect(customer_factory):
    with pytest.raises(ValueError) as e:
        test = customer_factory.create(email="a.com", is_staff=True, is_superuser=True)
    assert str(e.value) == "You must provide a valid email address"

def test_admin_not_staff(customer_factory):
    with pytest.raises(ValueError) as e:
        test = customer_factory.create(email="", is_staff=False, is_superuser=True)
    assert str(e.value) == "Superuser must be assigned to is_staff=True."
    
def test_admin_not_superuser(customer_factory):
    with pytest.raises(ValueError) as e:
        test = customer_factory.create(email="a.com", is_staff=True, is_superuser=False)
    assert str(e.value) == "Superuser must be assigned to is_superuser=True."
