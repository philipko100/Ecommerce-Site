import pytest
from account.forms import RegistrationForm


@pytest.mark.parametrize(
    "user_name, email, password, password2, validity",
    [
        ("user1", "a@a.com", "12345a", "12345a", True),
        ("", "a@a.com", "12345a", "12345a", False), # no username
        ("user1", "", "12345a", "12345a", False), # no email
        ("user1", "a@a.com", "12345a", "", False),  # no second password
        ("user1", "a@a.com", "12345a", "12345b", False),  # password mismatch
        ("user1", "a@.com", "12345a", "12345a", False),  # email
    ],
)
@pytest.mark.django_db
def test_create_account(user_name, email, password, password2, validity):
    form = RegistrationForm(
        data={
            "user_name": user_name,
            "email": email,
            "password": password,
            "password2": password2,
        },
    )
    assert form.is_valid() is validity

def test_account_register_redirect(client, customer_fixture):
    user = customer_fixture
    client.force_login(user)
    response = client.get("/account/register/")
    assert response.status_code == 302


@pytest.mark.django_db
def test_account_register_render(client):
    response = client.get("/account/register/")
    assert response.status_code == 200
