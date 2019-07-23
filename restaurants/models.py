from django.db import models

class Restaurant (models.Model): #calss name should always be singuler and start with Capital letter
    name = models.CharField(max_length=10)
    description = models.TextField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()

    def __str__(self):
     return self.name 