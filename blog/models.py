from django.db import models


# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    date = models.DateField()


#show the name instead of the default name Object
    def __str__(self):
        return self.title