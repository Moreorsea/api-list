# Generated by Django 2.2.14 on 2022-07-05 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20220306_1813'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Квартира')),
                ('square', models.CharField(max_length=100, verbose_name='Площадь')),
                ('floor', models.CharField(max_length=100, verbose_name='Этажность')),
                ('price', models.CharField(max_length=100, verbose_name='Цена')),
                ('count_room', models.CharField(choices=[('1к', '1к'), ('2к', '2к'), ('3к', '3к'), ('4к', '4к')], max_length=9, verbose_name='Количество комнат')),
                ('image', models.ImageField(upload_to='', verbose_name='Загрузить планировку')),
            ],
            options={
                'verbose_name': 'Квартиру',
                'verbose_name_plural': 'Квартира',
            },
        ),
    ]
