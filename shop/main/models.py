from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:  # Настройки модели в админке
        ordering = ('name',)  # Сортировка в админке по полю
        verbose_name = 'Категория'  # Название в админке
        verbose_name_plural = 'Категории' # Название в админке во множественном числе

    def  __str__(self):  # Отображение объекта котегории в админке
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)  # Связь между продуктами и категориями
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)  # upload_to - папка куда мы будем загружать картинки; blank=True - поле может быть пустое
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def  __str__(self):
        return self.name