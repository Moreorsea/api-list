from django.db import models

# Create your models here.


class Task(models.Model):
    description = models.CharField(max_length=140)
    color = models.CharField(max_length=10)
    due_date = models.DateTimeField('Дата выполнения', null=True, blank=True)
    is_archived = models.BooleanField('В архиве', default=False)
    is_favorite = models.BooleanField('В избранном', default=False)
    repeating_date = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задача'

    def __str__(self):
        return self.description
