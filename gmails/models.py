from django.db import models

# Create your models here.

class GooglePass(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.email} {self.password}'