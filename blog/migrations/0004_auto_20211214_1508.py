# Generated by Django 2.2.14 on 2021-12-14 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='i_work_nasa',
            field=models.BooleanField(verbose_name='Я работал в Nasa'),
        ),
    ]