# Generated by Django 4.1.3 on 2022-12-04 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0003_alter_tasks_ready_datatime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='ready_datatime',
            field=models.CharField(blank=True, max_length=255, verbose_name='Время готовности'),
        ),
    ]
