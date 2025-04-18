# Generated by Django 3.1.7 on 2025-04-14 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=140)),
                ('color', models.CharField(max_length=10)),
                ('due_date', models.DateTimeField(default='Null', verbose_name='Дата выполнения')),
                ('is_archived', models.BooleanField(default=False, verbose_name='В архиве')),
                ('is_favorite', models.BooleanField(default=False, verbose_name='В избранном')),
                ('repeating_days', models.CharField(default='Null', max_length=24)),
                ('dt', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания записи')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задача',
                'ordering': ('-dt',),
            },
        ),
    ]
