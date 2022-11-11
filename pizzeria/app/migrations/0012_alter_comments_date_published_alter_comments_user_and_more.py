# Generated by Django 4.1.2 on 2022-11-10 08:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_comments_text_alter_comments_date_published_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 10, 8, 42, 19, 114307, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='user',
            field=models.CharField(max_length=150, verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 10, 8, 42, 19, 109305, tzinfo=datetime.timezone.utc), verbose_name='дата'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_published',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 10, 8, 42, 19, 112303, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
    ]