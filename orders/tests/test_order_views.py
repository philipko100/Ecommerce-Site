import pytest
from django.urls.base import reverse
from orders.models import Order
from orders.views import payment_confirmation
from store.models import Category, Product


def test_payment_confirmation(order_fixture):
    payment_confirmation(order_fixture.order_key)
    assert Order.objects.get(order_key=order_fixture.order_key).billing_status

def test_order_add_view_order_exist(client, order_fixture):
    response = client.post(reverse("orders:add"), 
        data={"order_key": order_fixture.order_key,
                "action":"post"},)
    assert response.status_code == 200

@pytest.mark.django_db
def test_order_add_view_new_order(client, adminuser_fixture):
    user = adminuser_fixture
    client.force_login(user)
    Category.objects.create(name='django', slug='django')
    Product.objects.create(category_id=1, title='django beginners', description="product description",
                               slug='django-beginners', regular_price='20.00', discount_price="8.99" )
    client.post(
            reverse('basket:basket_add'), {"productid": 1, "productqty": 1, "action": "post"}, xhr=True)
        
    response = client.post(reverse("orders:add"), 
        data={"order_key": "unique!!123",
                "action":"post"},)
    assert response.status_code == 200
