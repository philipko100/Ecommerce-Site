# Ecommerce-Site

Ecommerce site where you can create an account, add items to cart, and purchase items at checkout.

This is a django project consisting of many django apps.

Commands to run this project:
1. py -m venv venv
2. venv\Scripts\activate
3. pip install -r requirements.txt
4. py manage.py runserver

To run this webapp, git clone this repository. Then go into the folder in a terminal, pip install requirements, and run "python ./manage.py runserver" and your terminal should return after some lines "Starting development server at http://127.0.0.1:8000/" or some other port number. Once you open the port link and create an account, look at the redirect screen or your console where you are running server for an activation link. IMPORTANT: Make sure to open that activation link or your account will not be useable.

To allow for Stripe integration when testing this web app, you must (on a terminal in the repo folder):
- However, to test fully with Stripe, you will need a Stripe account and a edit the keys and secrets for the Stripe APIs. Don't worry, you can still test checkout and all the other processes, but without the account, you won't be able to test successful purchases. If you do have a stripe account, do the following:  
1. pip install stripe
2. .\stripe login
3. .\stripe listen --forward-to localhost:8000/payment/webhook/

To access admin:
1. Go to (with the server running): http://127.0.0.1:8000/admin
2. email: a@a.com and password: admin <br>
If that doesn't work, you can always create your own superuser with "py manage.py createsuperuser"

In order to get started, you need to create a category: 
1. login
2. Go to Sell
3. Create Category

Then, after you create a category of your product, then you can upload your product to sell:
1. Go to Sell
2. Add Product
3. Use the Category you created in the form to add your product.
4. You can upload an image for your product. This product will automatically be "featured". 

Testing:

Testing in this webapp has been thoroughly done with python unit tests with django test and integration tests with pytest

To run tests, you can simply use "py manage.py test"

To run tests with coverage, you can use "coverage run --omit='#/venv/*' manage.py test" to run coverage on the relevant files of the webapp

To get coverage information after you run coverage, then you can view by "coverage report"
