from django.contrib import admin

# Register your models here.
from .models import Book
class Adminlog(admin.ModelAdmin):
    list_display=('title','author','coverimage')
admin.site.register(Book,Adminlog)