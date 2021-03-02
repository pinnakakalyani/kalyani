from .models import cart

def cart(request):
    return{'cart':cart(request)}