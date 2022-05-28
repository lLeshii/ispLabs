from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DeleteView
from cart.models import Order
# Create your views here.


class OrderListView(LoginRequiredMixin, ListView):
    template_name = "cart/orderlist.html"
    model = Order
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user).filter(
            Q(status="delivering") | Q(status="processing")).select_related('user').select_related('product')


class CartView(LoginRequiredMixin, ListView):
    template_name = "cart/cart.html"
    model = Order
    context_object_name = 'orders'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user, status="processing").select_related('user').select_related(
            'product')


class DeleteOrderView(LoginRequiredMixin, DeleteView):
    model = Order
    success_url = reverse_lazy("cart")


class DeleteOrderFromHistory(LoginRequiredMixin, DeleteView):
    model = Order
    success_url = reverse_lazy("orders")


class ClearCartView(LoginRequiredMixin, View):
    def post(self, request):
        cur_user = self.request.user
        Order.objects.filter(user=cur_user, status="processing").delete()

        return HttpResponseRedirect(reverse_lazy("cart"))


class CheckoutView(LoginRequiredMixin, View):
    def post(self, request):
        cur_user = self.request.user
        Order.objects.filter(user=cur_user, status="processing").update(status="delivering")

        return HttpResponseRedirect(reverse_lazy("cart"))
