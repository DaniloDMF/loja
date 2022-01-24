from pyexpat import model
from django.db import models

# Create your models here.
class cliente(models.Model):
    nome = models.CharField(max_length=50)
    senha = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id}: {self.nome} senha: {self.senha}" 