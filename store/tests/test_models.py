from account.models import UserBase
from django.test import TestCase
from django.urls import reverse
from store.models import Category, Product


class TestCategories(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    # test __str__ self function of model
    def test_category_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'django')

    # test view by category url
    def test_category_url(self):
        data = self.data1
        response = self.client.post(
            reverse('store:category_list', args=[data.slug]))
        self.assertEqual(response.status_code, 200)

class TestProductsModel(TestCase):

    def setUp(self):
        Category.objects.create(name='django', slug='django')
        UserBase.objects.create(user_name='admin', email="a@a.com")
        self.data1 = Product.objects.create(category_id=1, title='django test', description="product description",
                                                slug='django-test', regular_price='20.00', discount_price='8.99',)
    # test __str__ self function of model
    def test_products_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django test')

    # test view single product url
    def test_products_url(self):
        data = self.data1
        url = reverse('store:product_detail', args=[data.slug])
        self.assertEqual(url, '/django-test')
        response = self.client.post(
            reverse('store:product_detail', args=[data.slug]))
        self.assertEqual(response.status_code, 200)

    # test Product Manager which should only return all active products
    def test_products_custom_manager_basic(self):
        data = Product.objects.all()
        self.assertEqual(data.count(), 1)
