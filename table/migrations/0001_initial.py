# Generated by Django 4.1.3 on 2022-12-01 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=255, verbose_name='Фирма')),
                ('qty', models.CharField(blank=True, max_length=255, verbose_name='Шт.')),
                ('file_name', models.CharField(blank=True, max_length=255, verbose_name='Название')),
                ('plate_size', models.CharField(blank=True, max_length=255, verbose_name='Размер')),
                ('equipment', models.CharField(choices=[('BLUE', 'Синяя'), ('GREEN', 'Зелёная'), ('AURORA', 'Аврора B0'), ('THERMAL', 'Термальная'), ('FIRST', 'Первая')], default='Пусто', max_length=255, verbose_name='Машина')),
                ('add_data', models.DateField(auto_now_add=True, verbose_name='Дата')),
                ('add_time', models.TimeField(auto_now_add=True, verbose_name='Время')),
                ('punch', models.CharField(blank=True, choices=[('PUNCH', 'Панч'), ('PUNCH_BEND', 'Панч+Загиб')], max_length=255, verbose_name='Панч')),
                ('stage', models.BooleanField(default=False, verbose_name='Состояние')),
                ('operator', models.CharField(choices=[('YURA', 'Юрий'), ('ZIYO', 'Зийо'), ('AZIZ', 'Азиз'), ('DIMA', 'Дмитрий'), ('DEJURN', 'Дежурные')], default='Оператор', max_length=255, verbose_name='Вывел')),
                ('ready_datatime', models.DateTimeField(verbose_name='Время готовности')),
            ],
            options={
                'verbose_name': 'Задание',
                'verbose_name_plural': 'Задания',
            },
        ),
    ]
