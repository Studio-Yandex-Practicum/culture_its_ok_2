# Generated by Django 4.1 on 2023-08-20 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exhibit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Без названия', max_length=150, verbose_name='Название')),
                ('description', models.TextField(default='Без описания', verbose_name='Описание')),
                ('image', models.ImageField(upload_to='pictures', verbose_name='Фото')),
                ('address', models.TextField(verbose_name='Точный адрес')),
                ('author', models.CharField(default='Не указан', max_length=100, verbose_name='Автор')),
                ('how_to_pass', models.TextField(blank=True, verbose_name='Путь до объекта')),
                ('message_before_description', models.TextField(blank=True, verbose_name='Подводка')),
                ('reflection', models.TextField(blank=True, verbose_name='Рефлексии')),
                ('reflection_positive', models.TextField(blank=True, verbose_name='Сообщение после положительного ответа пользователя')),
                ('reflection_negative', models.TextField(blank=True, verbose_name='Сообщение после отрицательного ответа пользователя')),
                ('transfer_message', models.TextField(blank=True, verbose_name='Сообщение для перехода к следующему объекту')),
            ],
            options={
                'verbose_name': 'Объект',
                'verbose_name_plural': 'Объекты',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Без названия', max_length=150, verbose_name='Название')),
                ('description', models.TextField(default='Без описания', verbose_name='Описание')),
                ('image', models.ImageField(upload_to='pictures', verbose_name='Фото')),
                ('address', models.TextField(verbose_name='Точный адрес')),
                ('route_map', models.ImageField(upload_to='pictures', verbose_name='Карта маршрута')),
                ('text_route_start', models.TextField(blank=True, verbose_name='Текст к месту начала маршрута')),
            ],
            options={
                'verbose_name': 'Маршрут',
                'verbose_name_plural': 'Маршруты',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='RouteExhibit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exhibit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='culture.exhibit', verbose_name='Объекты')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='culture.route', verbose_name='Маршрут')),
            ],
            options={
                'verbose_name': 'Объект',
                'verbose_name_plural': 'Объекты',
            },
        ),
        migrations.AddField(
            model_name='route',
            name='exhibite',
            field=models.ManyToManyField(related_name='routes', through='culture.RouteExhibit', to='culture.exhibit'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='Аноним', max_length=100, verbose_name='Имя')),
                ('userage', models.IntegerField(blank=True, null=True, verbose_name='Возраст')),
                ('userhobby', models.CharField(default='Не указано', max_length=150, verbose_name='Хобби')),
                ('answer_to_message_before_description', models.TextField(blank=True, default='Вопроса не было.', verbose_name='Ответ на подводку')),
                ('answer_to_reflection', models.TextField(blank=True, default='Ответа не было.', verbose_name='Ответ на рефлексию')),
                ('exhibit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='culture.exhibit', verbose_name='Объект')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('text', models.TextField(verbose_name='Отзыв на маршрут')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='culture.route', verbose_name='Маршрут')),
            ],
            options={
                'verbose_name': 'Опрос',
                'verbose_name_plural': 'Опросы',
            },
        ),
        migrations.AddConstraint(
            model_name='routeexhibit',
            constraint=models.UniqueConstraint(fields=('route', 'exhibit'), name='unique_exhibites_route'),
        ),
    ]
