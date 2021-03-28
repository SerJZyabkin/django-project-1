from django.db import models

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