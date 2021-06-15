from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class NewsEntry:
    id : int
    name : str
    icon : str
    description : str

class LinkEntry:
    id: int
    name: str
    description: str
    extra_text: str
    image : str
    out_link : str


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