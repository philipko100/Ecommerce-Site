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
1. pip install stripe
2. .\stripe login
3. .\stripe listen --forward-to localhost:8000/payment/webhook/

To access admin:
1. Go to (with the server running): http://127.0.0.1:8000/admin
2. email: a@a.com and password: admin
