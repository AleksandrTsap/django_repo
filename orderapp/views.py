from django.db import transaction
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView

from orderapp.forms import OrderForm, OrderItemForm
from orderapp.models import Order, OrderItem


class OrderList(ListView):
    model = Order

    def get_queryset(self):
        return self.request.user.orders.all()


class OrderCreate(CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('orders:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=3)

        if self.request.POST:
            formset = OrderFormSet(self.request.POST, self.request.user)
        else:
            context['form'].initial['user'] = self.request.user
            basket_items = self.request.user.basket.all()
            if basket_items and basket_items.count():
                OrderFormSet = inlineformset_factory(
                    Order, OrderItem, form=OrderItemForm, extra=basket_items.count() + 1
                )
                formset = OrderFormSet()
                for form, basket_item in zip(formset.forms, basket_items):
                    form.initial['product'] = basket_item.product
                    form.initial['qty'] = basket_item.qty
            else:
                formset = OrderFormSet()
        context['orderitems'] = formset
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']

        with transaction.atomic():
            order = super().form_valid(form)
            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()
                self.request.user.basket.all().delete()

        if self.object.total_cost == 0:
            self.object.delete()

        return order


class OrderUpdate(UpdateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy('orders:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=1)
        if self.request.POST:
            formset = OrderFormSet(
                self.request.POST,
                self.request.FILES,
                instance=self.object
            )
        else:
            formset = OrderFormSet(instance=self.object)
        context['orderitems'] = formset
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']

        with transaction.atomic():
            order = super().form_valid(form)
            if orderitems.is_valid():
                orderitems.save()

        if self.object.total_cost == 0:
            self.object.delete()

        return order


def forming_complete(request, order_pk):
    order = get_object_or_404(Order, pk=order_pk)
    order.is_senden()
    order.save()
    return HttpResponseRedirect(reverse('orders:index'))