from decimal import Decimal
from django.conf import settings
from .models import cart

class items(object):
    def __init__(self, request):
        self.session=request.session
        cart=self.session.get(settings.ADDTOCART_SESSION_ID)
        if not cart:
            cart=self.session[settings.ADDTOCART_SESSION_ID] = {}
        self.cart=cart


    def __add__(self, cart,quantity=1, update_quantity=False):
        item_id=str(id)
        if item_id not in self.cart:
            self.cart[item_id]={'quantity':0,
                                'price':str(cart.price)}

        if update_quantity:
            self.cart[item_id]['quantity'] =quantity
        else:
            self.cart[item_id]['quantity']+=quantity
        self.save()

    def save(self):
        self.session[settings.ADDTOCART_SESSION_ID] = self.cart
        self.session.modified=True

    '''def remove(self,cart):
        item_id = self.cart.keys()
        item=cart.objects.filter(id__in)=item_id)
'''