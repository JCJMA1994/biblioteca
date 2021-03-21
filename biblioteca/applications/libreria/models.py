from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField('Nombres', max_length=80)
    nationality = models.CharField('Nacionalidad', blank=True, max_length=100)

    def __str__(self):
        return self.name