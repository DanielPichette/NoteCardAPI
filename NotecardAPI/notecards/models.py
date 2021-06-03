from django.db import models


# Create your models here.
class Collection(models.Model):
    name = models.CharField(max_length=50)
    notecards = models.ForeignKey('NotecardAPI.Notecard', default=None, null=True, on_delete=models.CASCADE)

    def __int__(self):
        return self.name


class Notecard(models.Model):
    word = models.CharField(max_length=50)
    definition = models.CharField(max_length=500)
    collection = models.ForeignKey('NotecardAPI.Collection', default=None, null=True, on_delete=models.CASCADE)

    def __int__(self):
        return self.word
