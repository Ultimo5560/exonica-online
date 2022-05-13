from .models import CarShop

# codigo inconcluso

def get_or_set_order_session(request):
    carshop_id = request.session.get('carshop_id', None)
    if carshop_id is None:
        order = CarShop()
        order.save()
        request.session['carshop_id'] = order.id
    else:
        try:
            order = CarShop.objects.get(id=carshop_id)
        except CarShop.DoesNoExist:
            order = CarShop()
            order.save()
            request.session['carshop_id'] = order.id
    
    if request.user.is_authenticated and order.user is None:
        order.user = request.user
        order.save()
    return order
