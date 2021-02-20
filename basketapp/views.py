from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse

from basketapp.models import BasketItem
from django_gb.settings import LOGIN_URL


@login_required
def index(request):
    basket = request.user.basket.all()
    context = {'page_title': 'корзина',
               'basket': basket
               }
    return render(request, 'basketapp/index.html', context)


@login_required
def add_to(request, product_pk):
    if LOGIN_URL in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(
            reverse('basic:product_page',
                    kwargs={'pk': product_pk})
        )
    basket_item, _ = BasketItem.objects.get_or_create(
        user=request.user,
        product_id=product_pk
    )
    basket_item.qty += 1
    basket_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def delete(request, basket_item_pk):
    item = get_object_or_404(BasketItem, pk=basket_item_pk)
    item.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def update(request, basket_item_pk, qty):
    if request.is_ajax():
        item = BasketItem.objects.filter(pk=basket_item_pk).first()
        if not item:
            return JsonResponse({'status': False})
        if qty == 0:
            item.delete()
        else:
            item.qty = qty
            item.save()
        basket_summary_html = render_to_string(template_name='basketapp/includes/basket_summary.html',
                                               request=request)
        product_cost = item.product.price * qty
        return JsonResponse({'status': True,
                             'basket_summary': basket_summary_html,
                             'basket_item_pk': basket_item_pk,
                             'product_cost': product_cost,
                             'qty': qty, })
