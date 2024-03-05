from django .db import models
from django.contrib import admin
class book(models.Model):
     book_no=models.IntegerField(primary_key=True)
     book_name=models.CharField(max_length=20)
     author_name=models.CharField(max_length=30)
     book_page=models.IntegerField()
     book_price=models.IntegerField()
     
class bookAdmin(admin.ModelAdmin):
    list_display=('book_no','book_name','author_name','book_page','book_price')