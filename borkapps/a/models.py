from django.db import models
from borkapps.b import models as models_b
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    best_author = models.ForeignKey(models_b.Author, null=True)

class Entry(models.Model):
    blog = models.ForeignKey(Blog)