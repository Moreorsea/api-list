from django.db import models

# Create your models here.


class Task(models.Model):
    description = models.CharField(max_length=140)
    color = models.CharField(max_length=10)
    due_date = models.DateTimeField('Дата выполнения', default="Null")
    is_archived = models.BooleanField('В архиве', default=False)
    is_favorite = models.BooleanField('В избранном', default=False)
    repeating_days = models.CharField(max_length=24, default="Null")
    dt = models.DateTimeField('Дата создания записи', auto_now_add=True)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задача'
        ordering = ('-dt',)

    def __str__(self):
        return self.description
