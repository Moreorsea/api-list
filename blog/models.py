from django.db import models
from django.urls import reverse

# Create your models here.


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
