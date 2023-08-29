from django.db import models

class Champions(models.Model):
    champions_name = models.CharField(max_length=40)
    champions_team = models.CharField(max_length=40)
    champions_year = models.DateField()

    def __str__(self):
        return self.champions_name