from account.models import UserBase
from django.test import TestCase
from django.urls import reverse
from store.models import Category, Product


class TestBasketView(TestCase):

    def setUp(self):
        UserBase.objects.create(user_name='admin', email="a@a.com")
        Category.objects.create(name='django', slug='django')
        Product.objects.create(category_id=1, title='django beginners', description="product description",
                               slug='django-beginners', regular_price='20.00', discount_price="8.99" )
        Product.objects.create(category_id=1, title='django intermediate', description="product description",
                               slug='django-intermediate', regular_price='20.00', discount_price="8.99")
        Product.objects.create(category_id=1, title='django advanced', description="product description",
                               slug='django-advanced', regular_price='20.00', discount_price="8.99")
        Product.objects.create(category_id=1, title='dicount product', description="product description",
                               slug='dicount-product', regular_price='20.00', discount_price="8.99", is_on_sale=True)
        self.client.post(
            reverse('basket:basket_add'), {"productid": 1, "productqty": 1, "action": "post"}, xhr=True)
        self.client.post(
            reverse('basket:basket_add'), {"productid": 2, "productqty": 2, "action": "post"}, xhr=True)
        self.client.post(
            reverse('basket:basket_add'), {"productid": 4, "productqty": 1, "action": "post"}, xhr=True)

    # test basket url response 
    def test_basket_url(self):
        response = self.client.get(reverse('basket:basket_summary'))
        self.assertEqual(response.status_code, 200)
    
    # test adding to basket
    def test_basket_add(self):
        response = self.client.post(
            reverse('basket:basket_add'), {"productid": 3, "productqty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 5})
        response = self.client.post(
            reverse('basket:basket_add'), {"productid": 2, "productqty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 6})
        response = self.client.post(
            reverse('basket:basket_add'), {"productid": 4, "productqty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 7})

    # test deleting a product in basket
    def test_basket_delete(self):
        response = self.client.post(
            reverse('basket:basket_delete'), {"productid": 2, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 2, 'subtotal': '28.99'})

    # test updating a quantity of a product in a basket
    def test_basket_update(self):
        response = self.client.post(
            reverse('basket:basket_update'), {"productid": 2, "productqty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 3, 'subtotal': '48.99'})
        response = self.client.post(
            reverse('basket:basket_update'), {"productid": 4, "productqty": 2, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 4, 'subtotal': '57.98'})

    # test deleting a product in basket
    def test_basket_clear(self):
        response = self.client.get(reverse('payment:order_placed'))
        response = self.client.post(
            reverse('basket:basket_add'), {"productid": 3, "productqty": 1, "action": "post"}, xhr=True)
        self.assertEqual(response.json(), {'qty': 1})
