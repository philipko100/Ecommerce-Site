import io

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls.base import reverse
from PIL import Image
from store.models import Product


@pytest.mark.parametrize(
    "category, validity",
    [
        ("category1", 200),
    ],
)
@pytest.mark.django_db
def test_create_category(client, category, validity):
    response = client.post("/inventory/add-category/", data={"name": category,},)
    assert response.status_code == validity

@pytest.mark.django_db
def test_create_category_get(client,):
    response = client.get("/inventory/add-category/",)
    assert response.status_code == 200

def generate_photo_file():
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file

@pytest.mark.django_db
def test_create_product_inventory(client, product_category_fixture,customer_fixture):
    user = customer_fixture
    client.force_login(user)
    # response = client.post("/inventory/add-category/", data={"name": "category1",},)
    image = generate_photo_file()
    response = client.post(
        "/inventory/add/",
        data={
            "category": product_category_fixture,
            "title":  "product title",
            "description":  "product description",
            "regular_price": 10.99,
            "discount_price": 8.99,
            "is_on_sale": False,
            "featured_image": image
        },
    )
    assert response.status_code == 200

@pytest.mark.django_db
def test_edit_product_inventory(client, product_fixture, customer_fixture):
    user = customer_fixture
    client.force_login(user)
    image = generate_photo_file()
    response = client.post(
        reverse('inventory:inventory_edit', args=[product_fixture.id]),
        data={
            "category": "newcategory",
            "title":  "product title",
            "description":  "product description",
            "regular_price": 10.99,
            "discount_price": 8.99,
            "is_on_sale": False,
            "featured_image": image
        },
    )
    assert response.status_code == 200

@pytest.mark.django_db
def test_create_product_inventory_get(client,):
    response = client.get("/inventory/add/",)
    assert response.status_code == 200

@pytest.mark.django_db
def test_create_product_inventory_edit_get(client, product_fixture):
    response = client.get(reverse('inventory:inventory_edit', args=[product_fixture.id]))
    assert response.status_code == 200

@pytest.mark.django_db
def test_inventory_summary(client, customer_fixture):
    user = customer_fixture
    client.force_login(user)
    response = client.get("/inventory/",)
    assert response.status_code == 200

@pytest.mark.django_db
def test_inventory_summary_admin(client, adminuser_fixture):
    user = adminuser_fixture
    client.force_login(user)
    response = client.get("/inventory/",)
    assert response.status_code == 200

@pytest.mark.django_db
def test_inventory_inactive(client, product_fixture):
    response = client.get(reverse('inventory:inventory_inactive', args=[product_fixture.id]))
    assert Product.objects.get(pk=product_fixture.id).is_active == False

@pytest.mark.django_db
def test_inventory_delete(client, product_fixture):
    response = client.get(reverse('inventory:inventory_delete', args=[product_fixture.id]))
    products = Product.objects.filter(pk=product_fixture.id)
    assert products.count() == 0
