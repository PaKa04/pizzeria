# Generated by Django 4.1.1 on 2022-10-09 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_pizza_ingridients'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='max 24 symbols', max_length=24, verbose_name='название')),
                ('descr', models.CharField(blank=True, help_text='max 140 symbols', max_length=140, null=True, verbose_name='описание')),
                ('is_published', models.BooleanField(default=False, verbose_name='publication')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.category', verbose_name='род. категория')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'db_table': 'app_categoies',
                'ordering': ('is_published', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Max 36 symbols', max_length=36, verbose_name='название')),
                ('descr', models.CharField(blank=True, help_text='Max 140 symbols', max_length=140, null=True, verbose_name='описание')),
                ('article', models.CharField(help_text='Max 16 symbols', max_length=16, verbose_name='артикль')),
                ('is_published', models.BooleanField(default=False, verbose_name='publication')),
                ('price', models.DecimalField(decimal_places=2, default=0, help_text='Max 999999.99', max_digits=8, verbose_name='цена')),
                ('category', models.ForeignKey(help_text='Max 16 symbols', on_delete=django.db.models.deletion.PROTECT, to='app.category', verbose_name='категория')),
            ],
            options={
                'db_table': 'app_products',
            },
        ),
        migrations.DeleteModel(
            name='Drinks',
        ),
        migrations.DeleteModel(
            name='Snacks',
        ),
    ]