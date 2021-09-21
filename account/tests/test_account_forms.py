import pytest
from account.forms import PwdResetForm, RegistrationForm


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

@pytest.mark.parametrize(
    "user_name, password, password2, validity",
    [
        ("user1", "12345a", "12345a", False),
    ],
)
@pytest.mark.django_db
def test_create_account_email_already_taken(user_name, password, password2, customer_fixture, validity):
    form = RegistrationForm(
        data={
            "user_name": user_name,
            "email": customer_fixture.email,
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

@pytest.mark.django_db
def test_reset_password_email_not_found():
    form = PwdResetForm(
            data={
                "email": "notfound@notfoundemail.com",
            },
        )
    assert form.is_valid() == False

@pytest.mark.django_db
def test_reset_password_email_found(customer_fixture):
    form = PwdResetForm(
            data={
                "email": customer_fixture.email,
            },
        )
    assert form.is_valid()
        