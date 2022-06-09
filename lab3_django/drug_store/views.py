from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

import drug_store.models
from cart.models import Order
from .forms import NewProductForm, NewCategoryForm
from .models import Category, Product
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from cart.forms import OrderForm
import logging
logger = logging.getLogger("main_logger")
logger.setLevel(logging.DEBUG)


class ProductListView(ListView):
    template_name = "drug_store/product/goods_list.html"
    model = Product
    context_object_name = 'products'
    logger.info("use ProductListView")


class CategoryListView(ListView):
    template_name = "drug_store/product/categoriests_list.html"
    model = Category
    context_object_name = 'categories'
    logger.info("use CategoryListView")


class CategoryDetailView(ListView):
    template_name = "drug_store/product/concr_categ.html"
    model = Product
    context_object_name = 'products'
    logger.info("use CategoryDetailView")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Product.category
        context['pk'] = self.kwargs['pk']
        return context

    def get_queryset(self):
        return Product.objects.filter(category_id=self.kwargs['pk']).select_related('category')


class ProductDetailView(DetailView):
    template_name = "drug_store/product/detail.html"
    model = Product
    context_object_name = 'product'
    logger.info("use DetailUserView")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm

        return context

class OrderCreationView(LoginRequiredMixin, FormView):
    form_class = OrderForm
    template_name = "drug_store/product/detail.html"
    logger.info("use OrderCreationView")

    def form_valid(self, form):
        product_id = self.kwargs['pk']
        order = form.save(commit=False)
        order.status = "processing"
        order.user = self.request.user
        order.product = get_object_or_404(Product, id=product_id)
        exists_order = Order.objects.filter(user=order.user, product=order.product, status="processing")
        if order.amount > order.product.stock:
            order.clean()
        elif exists_order:
            exists_order[0].amount += order.amount
            exists_order[0].save()
            param = order.product.stock - exists_order[0].amount
            if not order.user.is_superuser:
                Product.objects.filter(id=product_id).update(stock= param)
        else:
            order.save()
            param = order.product.stock - order.amount
            if not order.user.is_superuser:
                Product.objects.filter(id=product_id).update(stock=param)

        return HttpResponseRedirect(reverse_lazy("product_list"))

    def form_invalid(self, form):
        return HttpResponseRedirect(reverse_lazy("product_list"))


class CreateNewProduct(CreateView):
    form_class = NewProductForm
    template_name = 'drug_store/product/creating.html'
    success_url = reverse_lazy('product_list')
    logger.info("use CreateNewProduct")


class UpdtaeProduct(UpdateView):
    model = Product
    form_class = NewProductForm
    template_name = 'drug_store/product/redacting.html'
    success_url = reverse_lazy('product_list')
    logger.info("use UpdtaeProduct")


class DeleteProduct(DeleteView):
    model = Product
    success_url = reverse_lazy("product_list")
    logger.info("use DeleteProduct")


class CreateNewCategory(CreateView):
    form_class = NewCategoryForm
    template_name = 'drug_store/product/creating_cat.html'
    success_url = reverse_lazy('categories')
    logger.info("use CreateNewCategory")


class UpdateCategory(UpdateView):
    model = Category
    form_class = NewCategoryForm
    template_name = 'drug_store/product/redacting_cat.html'
    success_url = reverse_lazy('categories')
    logger.info("use UpdateCategory")


class DeleteCategory(DeleteView):
    model = Category
    success_url = reverse_lazy("categories")
    logger.info("use DeleteProduct")
