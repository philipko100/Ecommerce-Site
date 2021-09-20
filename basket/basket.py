from decimal import Decimal

from django.conf import settings
from store.models import Product


class Basket():

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if settings.BASKET_SESSION_ID not in request.session:
            basket = self.session[settings.BASKET_SESSION_ID] = {}
        self.basket = basket

    # returns iterable of all items in basket
    def __iter__(self):
        product_ids = self.basket.keys()
        products = Product.objects.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item

    # returns the quantity of items in baskeyt
    def __len__(self):
        return sum(item['qty'] for item in self.basket.values())

    # returns total price
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())

    def save(self):
        self.session.modified = True

    # adds product to the basket
    def add(self, product, qty):
        product_id = str(product.id)
        if product_id in self.basket:
            self.basket[product_id]['qty'] += qty
        else:
            if product.is_on_sale:
                self.basket[product_id] = {'price': str(product.discount_price), 'qty': qty}
            else:
                self.basket[product_id] = {'price': str(product.regular_price), 'qty': qty}
        self.save()
        
    # deletes the product in the basket
    def delete(self, product):
        product_id = str(product)
        if product_id in self.basket:
            del self.basket[product_id]
            self.save()

    # updates the quantity of a certain product in basket
    def update(self, product, qty):
        product_id = str(product)
        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
        self.save()

    # removes basket from session
    def clear(self):
        del self.session[settings.BASKET_SESSION_ID]
        self.save()
