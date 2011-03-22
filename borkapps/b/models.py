from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    contributed_to = models.ManyToManyField('a.Blog')

class AuthorEdit(models.Model):
    author = models.ForeignKey(Author)
    entry = models.ForeignKey('a.Entry')

