import factory
from account.models import UserBase
from faker import Faker
from inventory.models import InventoryItem
from orders.models import Order, OrderItem
from store.models import (
    Category,
    Product,
    ProductSpecification,
    ProductSpecificationValue,
    ProductType,
)

fake = Faker()

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    
    name = "django"
    slug = "django"

class ProductTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductType
        django_get_or_create = ("name",)

    name = "book"


class ProductSpecificationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductSpecification

    product_type = factory.SubFactory(ProductTypeFactory)
    name = "pages"


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
        django_get_or_create = ("slug",)

    category = factory.SubFactory(CategoryFactory)
    title = "product_title"
    description = fake.text()
    slug = "product_slug"
    regular_price = "9.99"
    discount_price = "4.99"
    is_on_sale = False

class ProductDiscountedFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    category = factory.SubFactory(CategoryFactory)
    title = "product_title"
    description = fake.text()
    slug = "product_slug"
    regular_price = "9.99"
    discount_price = "4.99"
    is_on_sale = True


class ProductSpecificationValueFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductSpecificationValue

    product = factory.SubFactory(ProductFactory)
    specification = factory.SubFactory(ProductSpecificationFactory)
    value = "100"


####
# Account
####


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserBase
        django_get_or_create = ("user_name",)

    email = "a@a.com"
    user_name = "user1"
    first_name = fake.name()
    phone_number = fake.phone_number()
    postcode = fake.postcode()
    address_line_1 = fake.street_address()
    address_line_2 = fake.street_address()
    town_city = fake.city()
    password = "tester"
    is_active = True
    is_staff = False

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        if "is_superuser" in kwargs:
            return manager.create_superuser(*args, **kwargs)
        else:
            return manager.create_user(*args, **kwargs)


class InventoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = InventoryItem

    user = factory.SubFactory(CustomerFactory)
    product = factory.SubFactory(ProductFactory)

class InventoryDiscountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = InventoryItem

    user = factory.SubFactory(CustomerFactory)
    product = factory.SubFactory(ProductDiscountedFactory)

class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order
        django_get_or_create = ("order_key",)

    user = factory.SubFactory(CustomerFactory)
    full_name = "user1"
    address1 = fake.street_address()
    address2 = fake.street_address()
    city = fake.city()
    phone = fake.phone_number()
    post_code = fake.postcode()
    total_paid = 99
    order_key = "sf3f23"
    billing_status = False

class OrderItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OrderItem

    order = factory.SubFactory(OrderFactory)
    product = factory.SubFactory(ProductFactory)
    price = 9
    quantity = 11
