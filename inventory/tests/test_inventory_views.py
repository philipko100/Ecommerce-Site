import io

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image


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
    response = client.post("/inventory/add-category/", data={"name": "category1",},)
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
def test_create_product_inventory_get(client,):
    response = client.get("/inventory/add/",)
    assert response.status_code == 200
