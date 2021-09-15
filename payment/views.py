from django.shortcuts import render
import json
import stripe
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from basket.basket import Basket


def order_placed(request):
    basket = Basket(request)
    basket.clear()
    return render(request, 'payment/orderplaced.html')


class Error(TemplateView):
    template_name = 'payment/error.html'


@login_required
def BasketView(request):
    basket = Basket(request)
    total = str(basket.get_total_price())
    total = total.replace('.', '')
    total = int(total)

    stripe.api_key = 'sk_test_51JZtewAxxrgwQLI9ZAzq1kbxQbG0s19jfdfjHG3nUq40vrv81QdDh6ut2xF5JPiVdIBr78wl8DgHMzaj0p8fupRD00wLRlEf99'
    intent = stripe.PaymentIntent.create(
        amount=total,
        currency='cad',
        metadata={'userid': request.user.id}
    )
    return render(request, 'payment/home.html', {'client_secret': intent.client_secret})