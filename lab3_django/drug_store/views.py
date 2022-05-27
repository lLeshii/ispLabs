from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.views.generic import ListView, DetailView

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
        #context['form'] = OrderCreationForm

        return context
