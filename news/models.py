from django.db import models

# Create your models here.
class New(models.Model):
    Headline = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateField()
    def __str__ (self) :
        return self.Headline
