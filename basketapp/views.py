from django.http import HttpResponseRedirect

from basketapp.models import BasketItem


def index(request):
    pass


def add_to(request, product_pk):
    basket_item, _ = BasketItem.objects.get_or_create(
        user=request.user,
        product_id=product_pk
    )
    basket_item.qty += 1
    basket_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete(request, pk):
    pass
