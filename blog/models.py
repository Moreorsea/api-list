from django.db import models
from django.urls import reverse

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField('Completed', default=False)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Запись'

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('died', null=True, blank=True)

    class Meta:
        verbose_name = 'Автора'
        verbose_name_plural = 'Авторы книг'

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)


class Genre(models.Model):
    name = models.CharField('Название жанра', max_length=100)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры книг'

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField('Название книги', max_length=100)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='book_author', verbose_name='Автор')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE,
                              related_name='book_genre', verbose_name='Жанр книги')
    description = models.TextField('Описание книги', max_length=1000)

    class Meta:
        verbose_name = 'Книгу'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.name


PROFESSION_LIST = (
    ('Инженер', 'Инженер'),
    ('Ученый', 'Ученый'),
    ('Психолог', 'Психолог'),
    ('Другая', 'Другая'),
)


class Application(models.Model):
    name = models.CharField('Ваше имя', max_length=100)
    email = models.EmailField('Почта')
    age = models.PositiveSmallIntegerField('Возраст')
    profession = models.CharField(
        'Профессия', max_length=9, choices=PROFESSION_LIST)
    i_work_nasa = models.BooleanField('Я работал в Nasa')
    file = models.FileField('Фото')

    class Meta:
        verbose_name = 'Заявку'
        verbose_name_plural = 'Заявка'

    def __str__(self):
        return self.name


class IrvacApply(models.Model):
    name = models.CharField('Ваше имя', max_length=100)
    phone = models.CharField('Номер телефона', max_length=11)
    dt = models.DateTimeField('Дата заявки', auto_now_add=True)

    class Meta:
        verbose_name = 'Заявку'
        verbose_name_plural = 'Заявка ИРВАС'

    def __str__(self):
        return self.name


TYPE_LIST = (
    ('Холодное', 'Холодное'),
    ('Теплое', 'Теплое'),
)


class IrvacFullApply(models.Model):
    form = models.CharField('Форма балкона', max_length=100)
    width = models.CharField('Ширина', max_length=100)
    height = models.CharField('Высота', max_length=100)
    type = models.CharField('Тип остекления', max_length=100)
    profile = models.CharField(
        'Тип остекления', max_length=9, choices=TYPE_LIST)
    name = models.CharField('Ваше имя', max_length=100)
    phone = models.CharField('Номер телефона', max_length=11)
    dt = models.DateTimeField('Дата заявки', auto_now_add=True)

    class Meta:
        verbose_name = 'Заявку'
        verbose_name_plural = 'Заявка ИРВАС замерщик'

    def __str__(self):
        return self.name


class Quiz(models.Model):
    question = models.CharField('Вопрос', max_length=100)
    answer_1 = models.CharField('1 ответ', max_length=100)
    answer_2 = models.CharField('2 ответ', max_length=100)
    answer_3 = models.CharField('3 ответ', max_length=100)
    answer_4 = models.CharField('4 ответ', max_length=100)
    answer_right = models.CharField('Верный ответ', max_length=100)

    class Meta:
        verbose_name = 'Квиз'
        verbose_name_plural = 'Квиз'

    def __str__(self):
        return self.question


class Switter(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    text = models.TextField('Текст сообщения', max_length=1000)
    likes = models.SmallIntegerField('Лайки')
    reposts = models.SmallIntegerField('Репосты')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты для Свиттера'

    def __str__(self):
        return self.title
