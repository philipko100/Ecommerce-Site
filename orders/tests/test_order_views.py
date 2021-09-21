import json
from importlib import import_module

from account.models import UserBase
from django.conf import settings
from django.test import Client, RequestFactory, TestCase
from django.urls.base import reverse
from faker import Faker
from store.models import Category, Product

fake = Faker()

class TestOrderView(TestCase):

    def setUp(self):
        self.c = Client()
        self.factory = RequestFactory()
        UserBase.objects.create(user_name='admin', email="a@a.com")
        Category.objects.create(name='django', slug='django')
        Product.objects.create(category_id=1, title='django beginners', description="product description",
                               slug='django-beginners', regular_price='20.00', discount_price="8.99" )
        self.client.post(
            reverse('basket:basket_add'), {"productid": 1, "productqty": 1, "action": "post"}, xhr=True)

    # def test_order_view_add(self):
    #     response = self.c.post(
    #         reverse('orders:add'),
    #         data={
    #             "order_key" : "sf3f23",
    #         },
    #     )
    #     print(response)
    #     assert "success" == response
