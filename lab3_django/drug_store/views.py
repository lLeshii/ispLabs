from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from cart.models import Order
from .forms import NewProductForm
from .models import Category, Product
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from cart.forms import OrderForm
from django.views import View


# def product_list(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     products = Product.objects.filter(available=True)
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)
#     return render(request,
#                   'drug_store/product/list.html',
#                   {'category': category,
#                    'categories': categories,
#                    'products': products})
#
#
# def product_detail(request, id, slug):
#     product = get_object_or_404(Product, id=id, slug=slug, available=True)
#     return render(request, 'drug_store/product/detail.html', {'product': product})
#

class ProductListView(ListView):
    template_name = "drug_store/product/goods_list.html"
    model = Product
    context_object_name = 'products'


class CategoryListView(ListView):
    template_name = "drug_store/product/categoriests_list.html"
    model = Category
    context_object_name = 'categories'


class CategoryDetailView(ListView):
    template_name = "drug_store/product/concr_categ.html"
    model = Product
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs['pk']

        return context

    def get_queryset(self):
        return Product.objects.filter(category_id=self.kwargs['pk']).select_related('category')


class ProductDetailView(DetailView):
    template_name = "drug_store/product/detail.html"
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm

        return context


class OrderCreationView(LoginRequiredMixin, FormView):
    form_class = OrderForm
    template_name = "drug_store/product/detail.html"

    def form_valid(self, form):
        product_id = self.kwargs['pk']
        order = form.save(commit=False)
        order.status = "processing"
        order.user = self.request.user
        order.product = get_object_or_404(Product, id=product_id)
        exists_order = Order.objects.filter(user=order.user, product=order.product, status="processing")
        if exists_order:
            exists_order[0].amount += order.amount
            exists_order[0].save()
        else:
            order.save()

        return HttpResponseRedirect(reverse_lazy("product_list"))

    def form_invalid(self, form):
        return HttpResponseRedirect(reverse_lazy("product_list"))


class CreateNewProduct(CreateView):
    form_class = NewProductForm
    template_name = 'drug_store/product/creating.html'
    success_url = reverse_lazy('product_list')


class UpdtaeProduct(UpdateView):
    model = Product
    form_class = NewProductForm
    template_name = 'drug_store/product/redacting.html'
    success_url = reverse_lazy('product_list')


class DeleteProduct(DeleteView):
    model = Product
    success_url = reverse_lazy("product_list")
