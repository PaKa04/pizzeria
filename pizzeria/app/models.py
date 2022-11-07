from django.db import models
from django.conf import settings
from django.utils.timezone import now
# Create your models here.


class Ingridients(models.Model):
    name = models.CharField(
        max_length=24,
        verbose_name='ингридиент',
        help_text='max 24 symbols'
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=5,
        default=0,
        verbose_name='цена',
        help_text='Max 999.99'
    )
    image = models.ImageField(
        upload_to='products',
        verbose_name="картинка",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'app_ingridients'


class Pizza(models.Model):
    name = models.CharField(
        max_length=24,
        verbose_name='пицца',
        help_text='max 24 symbols'
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=5,
        default=0,
        verbose_name='цена',
        help_text='Max 999.99'
    )
    ingridients = models.ManyToManyField(
        'ingridients',
        verbose_name='ингридиенты',
        related_name='ingridient'
    )
    descr = models.CharField(
        max_length=140,
        null=True,
        blank=True,
        verbose_name='описание',
        help_text="Max 140 symbols"
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='publication'
    )
    image = models.ImageField(
        upload_to='products',
        verbose_name="картинка",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "app_pizza"


class Category(models.Model):
    name = models.CharField(
        max_length=24,
        verbose_name='название',
        help_text='max 24 symbols'
    )
    parent = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="род. категория"
    )
    descr = models.CharField(
        max_length=140,
        blank=True,
        null=True,
        verbose_name='описание',
        help_text='max 140 symbols'
    )
    is_published = models.BooleanField(default=False, verbose_name='publication')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'app_categoies'
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ('is_published', 'name')


class Product(models.Model):
    title = models.CharField(
        max_length=36,
        verbose_name='название',
        help_text='Max 36 symbols'
    )
    descr = models.CharField(
        max_length=140,
        null=True,
        blank=True,
        verbose_name='описание',
        help_text="Max 140 symbols"
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='publication'
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=8,
        default=0,
        verbose_name='цена',
        help_text="Max 999999.99"
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        verbose_name='категория',
        help_text="Max 16 symbols"
    )
    image = models.ImageField(
        upload_to='products',
        verbose_name="картинка",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = "app_products"


class Contact(models.Model):
    name = models.CharField(max_length=64, verbose_name='имя')
    email = models.CharField(max_length=77, verbose_name='почта')
    message = models.CharField(max_length=1024, verbose_name='сообщение')
    date_created = models.DateTimeField(
        default=now(),
        verbose_name='дата'
    )

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'app_contacts'
        ordering = ('date_created', )
        verbose_name = 'обращение'
        verbose_name_plural = 'обращения'


class Cart(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='пользователь',
        on_delete=models.DO_NOTHING
    )
    name = models.CharField(
        max_length=120,
        verbose_name='название'
    )

    price = models.DecimalField(
        decimal_places=2,
        max_digits=8,
        default=0,
        verbose_name='цена',
        help_text="Max 999999.99"
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'app_carts'
        verbose_name = 'корзина'
        verbose_name_plural = 'корзины'

# class Order(models.Model):
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         verbose_name='пользователь',
#         on_delete=models.DO_NOTHING
#     )
#     pizza = models.ForeignKey(
#         'Pizza',
#         verbose_name='пицца',
#         on_delete=models.DO_NOTHING
#     )
#     drinks = models.ForeignKey(
#         'Drinks',
#         verbose_name='напитки',
#         on_delete=models.DO_NOTHING
#     )
#     snacks = models.ForeignKey(
#         'Snacks',
#         verbose_name='закуски',
#         on_delete=models.DO_NOTHING
#     )
#     date_created = models.DateTimeField(
#         auto_now_add=True,
#         verbose_name='дата'
#     )
#     price = models.DecimalField(
#         decimal_places=2,
#         max_digits=6,
#         default=0,
#         verbose_name='цена',
#         help_text='Max 9999.99'
#     )
#     is_paid = models.BooleanField(
#         default=False,
#         verbose_name='статус заказа'
#     )
#
#     def __str__(self):
#         return f'пользователь: {self.user}   заказ: {self.pizza}'
#
#     class Meta:
#         db_table = 'app_orders'
#         ordering = ('date_created',)
#         verbose_name = 'заказ'
#         verbose_name_plural = 'заказы'
