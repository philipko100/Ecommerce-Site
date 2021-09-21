import io

import pytest
from inventory.forms import ProductAddForm
from PIL import Image


def generate_photo_file():
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file
        
@pytest.mark.django_db
def test_product_add_form(product_category_fixture):
    image = generate_photo_file()
    form = ProductAddForm(
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
    assert form.is_valid() == False
