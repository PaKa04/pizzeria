from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.urls import reverse
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


class Post(models.Model):

    title = models.CharField(
        max_length=24,
        verbose_name='title'
    )
    subtitle = models.CharField(
        max_length=24,
        verbose_name='Если был такой title',
        null=True,
        blank=True
    )
    preshow_text = models.CharField(
        max_length=90,
        verbose_name='Текст отображаемый в блоге',
        help_text='MAX 90 symbols',
        default='вам следует это прочитать'
    )
    first_text = models.TextField(
        verbose_name='first text'
    )
    image_of_post1 = models.ImageField(
        upload_to='posts/',
        verbose_name='image of post1',
        help_text='Обязательно'
    )
    image_of_post2 = models.ImageField(
        upload_to='posts/',
        verbose_name='image of post2',
        null=True,
        blank=True
    )
    second_text = models.TextField(
        verbose_name='second text'
    )
    last_text = models.TextField(
        verbose_name='last text',
        null=True,
        blank=True
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name='is published'
    )
    date_published = models.DateTimeField(
        default=now(),
        verbose_name='date published'
    )
    author = models.CharField(
        max_length=24,
        verbose_name='Автор',
        default='Pizzeria'
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='URL'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        db_table = 'blog_posts'
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        ordering = ('date_published', )


class Comments(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='пользователь',
        on_delete=models.DO_NOTHING
    )
    date_published = models.DateTimeField(
        default=now(),
        verbose_name='date published'
    )
    post = models.ForeignKey(
        Post,
        verbose_name='Post',
        on_delete=models.DO_NOTHING
    )

    def __str__(self):
        return self.user

    class Meta:
        db_table = 'app_comments'
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ('date_published',)
