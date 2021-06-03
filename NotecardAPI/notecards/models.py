from django.db import models


# Create your models here.
class Collection(models.Model):
    name = models.CharField(max_length=50)

    def __int__(self):
        return self.name


class Notecard(models.Model):
    word = models.CharField(max_length=50)
    definition = models.CharField(max_length=500)
    collection = models.ForeignKey('Collection', default=None, null=True, on_delete=models.CASCADE)

    def __int__(self):
        return self.word
