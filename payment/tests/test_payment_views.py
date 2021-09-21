import pytest
from django.urls.base import reverse
from store.models import Category, Product


@pytest.mark.django_db
def test_payment_basket_view(client, customer_fixture):
    user = customer_fixture
    client.force_login(user)
    Category.objects.create(name='django', slug='django')
    Product.objects.create(category_id=1, title='django beginners', description="product description",
                               slug='django-beginners', regular_price='20.00', discount_price="8.99" )
    client.post(
            reverse('basket:basket_add'), {"productid": 1, "productqty": 1, "action": "post"}, xhr=True)
        
    response = client.get(reverse("payment:basket"),)
    assert response.status_code == 200

@pytest.mark.django_db
def test_payment_webhook(client, customer_fixture):
    user = customer_fixture
    client.force_login(user)
    response = client.post("/payment/webhook/",
        data={
                "payment_intent.notsuccess": "not success"
            },)
    assert response.status_code == 400
