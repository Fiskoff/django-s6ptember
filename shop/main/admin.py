
from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']  # Список содержит те поля которые будут выводиться в админке
    prepopulated_fields = {'slug': ('name',)}  # Поле slug будет заполнятся на основе поля name


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated', 'category']  # Поля для фильтрации записей
    list_editable = ['price', 'available']  # Поля для обновления
    prepopulated_fields = {'slug': ('name',)}