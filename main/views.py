from django.shortcuts import render, get_object_or_404
from datetime import datetime
from main.models import Product
from django.views.generic import ListView, DetailView


# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'main/index.html'


def contacts(request):
    """Контроллер, который отвечает за отображение контактной информации."""

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone, message)

    return render(request, 'main/contacts.html')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product.html'


def great_prod(request):
    """Представление страницы main/great_prod.html с формой загрузки нового прожукта"""
    product_for_create = []
    if request.method == 'POST':
        product = {
            'name_prod': request.POST.get('name'),
            'description_prod': request.POST.get('description'),
            'category_prod': request.POST.get('category'),
            'price_prod': request.POST.get('price'),
            'data_create_prod': datetime.now(),
            'data_change_prod': datetime.now()
        }
        product_for_create.append(
            Product(**product)
        )
        # загрузка нового продукта в БД
        Product.objects.bulk_create(product_for_create)

    return render(request, 'main/great_prod.html')
