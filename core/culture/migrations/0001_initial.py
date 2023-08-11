# Generated by Django 4.1 on 2023-08-11 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='Имя')),
                ('userage', models.IntegerField(blank=True, null=True, verbose_name='Возраст')),
                ('userhobby', models.CharField(max_length=150, verbose_name='Хобби')),
                ('text', models.TextField(verbose_name='Отзыв')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='media/', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Маршрут',
                'verbose_name_plural': 'Маршруты',
            },
        ),
        migrations.CreateModel(
            name='Exhibit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='media/', verbose_name='Фото')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route', to='culture.route')),
            ],
            options={
                'verbose_name': 'Экспонат',
                'verbose_name_plural': 'Экспонаты',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='Имя')),
                ('userage', models.IntegerField(blank=True, null=True, verbose_name='Возраст')),
                ('userhobby', models.CharField(max_length=150, verbose_name='Хобби')),
                ('text', models.TextField(verbose_name='Отзыв')),
                ('exhibit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exhibit', to='culture.exhibit')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]