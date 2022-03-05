# Generated by Django 2.2.14 on 2022-01-21 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20220107_1645'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100, verbose_name='Вопрос')),
                ('answer_1', models.CharField(max_length=100, verbose_name='1 ответ')),
                ('answer_2', models.CharField(max_length=100, verbose_name='2 ответ')),
                ('answer_3', models.CharField(max_length=100, verbose_name='3 ответ')),
                ('answer_4', models.CharField(max_length=100, verbose_name='4 ответ')),
                ('answer_right', models.CharField(max_length=100, verbose_name='Верный ответ')),
            ],
            options={
                'verbose_name': 'Квиз',
                'verbose_name_plural': 'Квиз',
            },
        ),
        migrations.CreateModel(
            name='Switter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('text', models.TextField(max_length=1000, verbose_name='Текст сообщения')),
                ('likes', models.SmallIntegerField(verbose_name='Лайки')),
                ('reposts', models.SmallIntegerField(verbose_name='Репосты')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты для Свиттера',
            },
        ),
    ]