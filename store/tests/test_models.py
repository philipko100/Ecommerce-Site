from django.test import TestCase
from store.models import Category, Product
from django.contrib.auth.models import User


class TestCategories(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    # test __str__ self function of model
    def test_category_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'django')

class TestProductsModel(TestCase):

    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='django test',
                                                created_by_id=1, slug='django-test', price='20.00',
                                                image='django')
    # test __str__ self function of model
    def test_products_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django test')
