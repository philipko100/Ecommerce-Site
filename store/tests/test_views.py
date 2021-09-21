from importlib import import_module
from unittest import skip

from account.models import UserBase
from django.conf import settings
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse
from store.models import Category, Product
from store.views import product_all


class TestViewResponse(TestCase):
    
    def setUp(self) -> None:
        self.c = Client()
        self.factory = RequestFactory()
        Category.objects.create(name='django', slug='django')
        UserBase.objects.create(user_name='admin', email="a@a.com")
        self.data1 = Product.objects.create(category_id=1, title='django test', description='product description',
                                                slug='django-test', regular_price='20.00', discount_price='9.99',)
    
    # test allowed url hosts
    def test_url_allowed_hosts(self):
        response = self.c.get('/', HTTP_HOST='noaddress.com')
        self.assertEquals(response.status_code, 400)
        response = self.c.get('/', HTTP_HOST='yourdomain.com')
        self.assertEqual(response.status_code, 200)

    # test allowed hosts urls
    def test_url_allowed_hosts(self):
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    # test the dynamic url for the item detail page url
    def test_product_detail_url(self):
        response = self.c.get(reverse('store:product_detail', args=['django-test']))
        self.assertEqual(response.status_code, 200)

    def test_wrong_product_detail_url(self):
        response = self.c.get(reverse('store:product_detail', args=['django-wrong']))
        self.assertEqual(response.status_code, 404)

    # test the dynamic url for the item detail page url
    def test_category_list_url(self):
        response = self.c.get(reverse('store:category_list', args=['django']))
        self.assertEqual(response.status_code, 200)

    def test_wrong_category_list_url(self):
        response = self.c.get(reverse('store:category_list', args=['django-wrong']))
        self.assertEqual(response.status_code, 404)

    # test getting the homepage html
    def test_homepage(self):
        request = HttpRequest()
        engine = import_module(settings.SESSION_ENGINE)
        request.session = engine.SessionStore()
        response = product_all(request)
        html = response.content.decode('utf8')
        self.assertIn("<title>Philip's Store</title>", html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

    # also test getting homepage html with Request Factory
    def test_view_function(self):
        request = self.factory.get('/django-test')
        engine = import_module(settings.SESSION_ENGINE)
        request.session = engine.SessionStore()
        response = product_all(request)
        html = response.content.decode('utf8')
        self.assertIn("<title>Philip's Store</title>", html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)
