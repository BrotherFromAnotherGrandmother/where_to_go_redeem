from django.db import models


# Create your models here.

class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.CharField(max_length=400)
    description_long = models.TextField()

    def __str__(self):
        return self.title


class Image(models.Model):
    number = models.IntegerField()
    image = models.ImageField()
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number) + ' ' + str(self.place)
