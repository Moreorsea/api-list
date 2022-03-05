from django.contrib import admin
from .models import Author, Genre, Book, Application, IrvacApply, \
    IrvacFullApply, Switter

# Register your models here.
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Application)
admin.site.register(IrvacApply)
admin.site.register(IrvacFullApply)
admin.site.register(Switter)
