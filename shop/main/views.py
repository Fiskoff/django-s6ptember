from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def product_list(request, category_slug=None):
    categories = Category.objects.all()  # Вернёт все категории из БД
    products = Product.objects.filter(available=True)  # Вернёт все продукты, где available = True

    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)  # get_object_or_404 вернёт объект или 404 если объекта нет (объект, которому принадлежит этот slug)
        products = products.filter(category=category)

    return render(
        request,
        'main/product/list.html',  #  Шаблон позволяет вывести данные с бэкенд в формате html
        {                               # Контекст это то что мы передаём в шаблон. Вшаблоне для получения данных мы будем обращаться к объекту контекст
            'category': category,
            'categories': categories,
            'products': products
        }
    )