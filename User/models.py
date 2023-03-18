from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    phone = models.IntegerField()
    data_joined = models.DateTimeField(auto_now_add=True)
    data_de_nascimento = models.DateField()


    def __str__(self):
        return self.name

