from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class NewsEntry(models.Model):
    name = models.TextField()
    icon = models.CharField(max_length=100)
    description = RichTextUploadingField()


class ProductGroupEntry(models.Model):
    name = models.TextField()
    description = models.TextField()
    extra_text = models.TextField()
    image = models.ImageField(upload_to='pics')
    product_group_num = models.IntegerField()


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    img_left = models.ImageField(upload_to='img')
    desc_right = models.TextField()
    img_bot = models.ImageField(upload_to='img')
    desc_bot = models.TextField()


class Product(models.Model):
    ident = models.CharField(max_length=100)
    table = models.CharField(max_length=100)
    label = models.CharField(max_length=22)

class TableDefinition:
    ident : str
    column_names : list
    content : list