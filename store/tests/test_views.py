from django.test import TestCase, Client, RequestFactory
from unittest import skip
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpRequest
from store.models import Category, Product
from store.views import all_products

class TestViewResponse(TestCase):
    
    def setUp(self) -> None:
        self.c = Client()
        self.factory = RequestFactory()
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='django test',
                                                created_by_id=1, slug='django-test', price='20.00',
                                                image='django')

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
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Home</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

    # also test getting homepage html with Request Factory
    def test_view_function(self):
        request = self.factory.get('/item/django-test')
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Home</title>', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)
