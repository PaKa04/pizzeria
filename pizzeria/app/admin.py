from django.contrib import admin
from .models import Pizza, Category, Product, Ingridients, Contact, Cart, Post, Comments


# Register your models here.


class ProductTabularInline(admin.TabularInline):
    model = Product


@admin.action(description='Опубликовать')
def make_published(self, request, queryset):
    queryset.update(is_published=True)


@admin.action(description='Убрать  публикацию')
def make_unpublished(self, request, queryset):
    queryset.update(is_published=False)


@admin.register(Ingridients)
class IngridientsAdmin(admin.ModelAdmin):
    empty_value_display = 'Н/У'
    list_display = ('name', 'price')
    list_filter = ('name', 'price')
    search_fields = ('id', 'name')
    search_help_text = 'Введите имя ингридиента или id'
    actions = (make_unpublished, make_published)


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    empty_value_display = 'Н/У'
    list_display = ('name', 'price', 'is_published')
    list_filter = ('name', 'price')
    search_fields = ('id', 'name')
    search_help_text = 'Введите имя пиццы или id'
    filter_horizontal = ['ingridients']
    actions = (make_unpublished, make_published)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = 'Н/У'
    actions = (make_unpublished, make_published)
    list_display = ('name', 'parent', 'is_published')
    list_filter = ('is_published', 'parent')
    search_fields = ('id', 'name')
    search_help_text = 'Введите имя родительской категории или id'
    inlines = (ProductTabularInline,)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    empty_value_display = 'Н/У'
    actions = (make_published, make_unpublished)
    list_display = ('title', 'category', 'price', 'is_published')
    list_filter = ('is_published', 'category')
    search_fields = ('title', "id", 'price')
    search_help_text = 'заголовок/артикль/цена/id'
    fieldsets = (
        ('Основные настройки', {
            'fields': ('title', 'price',  'category'),
            'description': "describe"
        }),
        ('Дополнительные настройки', {
            'fields': ('is_published', 'descr', 'image')
        })
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_created'
    list_display = ('name', 'email', 'date_created')
    list_filter = ('name', 'email')


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    empty_value_display = 'Нафиг надо'
    list_display = ('name', 'user')
    list_filter = ('user', 'name')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', 'subtitle')}
    list_display = ('title', 'slug', 'date_published')
    date_hierarchy = 'date_published'
    list_filter = ('is_published', )
    readonly_fields = ('date_published', )
    actions = (make_published, make_unpublished)
    search_fields = ('title', 'id', 'subtitle')


@admin.register(Comments)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'date_published',)
