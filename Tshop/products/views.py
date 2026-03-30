from django.shortcuts import render
from .models import Product


from django.views.generic import(
    CreateView,
    ListView, DetailView,
    UpdateView,
    DeleteView
)

from django.urls import reverse_lazy


# Create your views here.
class ProductList(ListView):
    template_name = 'products/product_list.html'
    model = Product
    context_object_name = 'products'

class ProductDetailView(DetailView):
    template_name = 'products/product_details.html'
    model = Product
    context_object_name = 'product'

class AddProduct(CreateView):
    model = Product
    template_name = 'products/add_product.html'
    fields = '__all__'
    success_url = reverse_lazy('product_list')


class UpdateProduct(UpdateView):
    model = Product
    template_name = 'products/edit_product.html'
    fields = '__all__'
    success_url = reverse_lazy('product_list')


class DeleteProduct(DeleteView):
    model = Product
    template_name = 'products/del_product.html'
    success_url = reverse_lazy('product_list')
    context_object_name = 'product' 


