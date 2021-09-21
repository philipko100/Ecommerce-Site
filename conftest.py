import pytest
from pytest_factoryboy import register

from inventory.models import InventoryItem
from tests.factories import (
    CategoryFactory,
    CustomerFactory,
    InventoryDiscountFactory,
    InventoryFactory,
    OrderFactory,
    OrderItemFactory,
    ProductDiscountedFactory,
    ProductFactory,
    ProductSpecificationFactory,
    ProductSpecificationValueFactory,
    ProductTypeFactory,
)

register(CategoryFactory)
register(ProductTypeFactory)
register(ProductSpecificationFactory)
register(ProductFactory)
register(ProductDiscountedFactory)
register(ProductSpecificationValueFactory)
register(CustomerFactory)
register(InventoryFactory)
register(OrderFactory)
register(OrderItemFactory)
register(InventoryDiscountFactory)

@pytest.fixture
def product_category_fixture(db, category_factory):
    category = category_factory.create()
    return category

@pytest.fixture
def product_type_fixture(db, product_type_factory):
    product_type = product_type_factory.create()
    return product_type

@pytest.fixture
def product_specification_fixture(db, product_specification_factory):
    product_spec = product_specification_factory.create()
    return product_spec


@pytest.fixture
def product_fixture(db, product_factory):
    product = product_factory.create()
    return product

@pytest.fixture
def product_discounted_fixture(db, product_discounted_factory):
    product = product_discounted_factory.create()
    return product


@pytest.fixture
def product_spec_value_fixture(db, product_specification_value_factory):
    product_spec_value = product_specification_value_factory.create()
    return product_spec_value


@pytest.fixture
def customer_fixture(db, customer_factory):
    new_customer = customer_factory.create()
    return new_customer


@pytest.fixture
def adminuser_fixture(db, customer_factory):
    new_customer = customer_factory.create(user_name="admin_user", is_staff=True, is_superuser=True)
    return new_customer

@pytest.fixture
def inventory_fixture(db, inventory_factory):
    inventory = inventory_factory.create()
    inventory.user = customer_fixture
    inventory.product = product_fixture
    return inventory

@pytest.fixture
def inventory_discount_fixture(db, inventory_discount_factory):
    inventory = inventory_discount_factory.create()
    return inventory

@pytest.fixture
def order_fixture(db, order_factory):
    inventory = order_factory.create()
    return inventory

@pytest.fixture
def order_item_fixture(db, order_item_factory):
    inventory = order_item_factory.create()
    return inventory
