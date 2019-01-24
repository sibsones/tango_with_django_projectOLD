from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0, unique=False)
    likes = models.IntegerField(default=0, unique=False)


    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0, unique=False) # IntegerField Model 

    def __str__(self):
        return self.title

# Create your models here.
