import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_dashboard_url(client, customer_fixture):
    user = customer_fixture
    client.force_login(user)
    url = reverse("account:dashboard")
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_dashboard_url_notlogin(client):
    url = reverse("account:dashboard")
    response = client.get(url)
    assert response.status_code == 302

@pytest.mark.parametrize(
    "user_name, email, password, password2, validity",
    [
        ("user1", "a@a.com", "12345a", "12345a", 200),
        ("user1", "a@a.com", "12345a", "12345", 400),
        ("user1", "", "12345a", "12345", 400),
    ],
)
@pytest.mark.django_db
def test_create_account_view(client, user_name, email, password, password2, validity):
    response = client.post(
        "/account/register/",
        data={
            "user_name": user_name,
            "email": email,
            "password": password,
            "password2": password2,
        },
    )
    assert response.status_code == validity

@pytest.mark.parametrize(
    "email, user_name, first_name, validity,",
    [
        ("a@a.com", "user1", "firstname", 200),
    ],
)
@pytest.mark.django_db
def test_edit_account_view_post(client, email, user_name, first_name, validity, customer_fixture):
    user = customer_fixture
    client.force_login(user)
    response = client.post(
        "/account/profile/edit/",
        data={
            "email": email,
            "user_name": user_name,
            "first_name": first_name,
        },
    )
    assert response.status_code == validity

@pytest.mark.django_db
def test_edit_account_view_get(client, customer_fixture,):
    user = customer_fixture
    client.force_login(user)
    response = client.get(
        "/account/profile/edit/",
    )
    assert response.status_code == 200

@pytest.mark.django_db
def test_edit_account_delete(client, customer_fixture,):
    user = customer_fixture
    client.force_login(user)
    response = client.get(
        "/account/profile/delete_user/",
    )
    assert response.status_code == 302

