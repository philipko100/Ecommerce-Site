import pytest
from django.urls import reverse


def test_category_str(product_category_fixture):
    assert product_category_fixture.__str__() == "django"

def test_category_reverse(client, product_category_fixture):
    category = product_category_fixture
    url = reverse("store:category_list", args=[category])
    response = client.get(url)
    assert response.status_code == 200

def test_product_type_str(product_type_fixture):
    assert product_type_fixture.__str__() == "book"

def test_product_specification_str(product_specification_fixture):
    assert product_specification_fixture.__str__() == "pages"

def test_product_str(product_fixture):
    assert product_fixture.__str__() == "product_title"

def test_product_url_resolve(client, product_fixture):
    slug = "product_slug"
    url = reverse("store:product_detail", args=[slug])
    response = client.get(url)
    assert response.status_code == 200

def test_product_specification_value(product_spec_value_fixture):
    assert product_spec_value_fixture.__str__() == "100"
