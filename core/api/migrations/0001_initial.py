# Generated by Django 5.0.6 on 2024-06-05 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок объявления')),
                ('advert_id', models.IntegerField(unique=True, verbose_name='ID')),
                ('author', models.CharField(max_length=100, verbose_name='Автор объявления')),
                ('views_count', models.IntegerField(verbose_name='Количество просмотров')),
                ('position', models.IntegerField(null=True, verbose_name='Позиция объявления')),
            ],
        ),
    ]
