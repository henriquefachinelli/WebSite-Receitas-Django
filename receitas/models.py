from distutils.command.upload import upload
from django.db import models
from datetime import datetime

def upload_image_receita(instance, filename):
    return f"{instance.nome_receita} - {filename}"

class Receita(models.Model):
    nome_receita = models.CharField(unique=True, max_length=200)
    ingredientes = models.TextField()
    preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    dt_prepato = models.DateTimeField(default=datetime.now, blank=True)
    file_name = models.ImageField(upload_to='', null=False)  


    def __str__(self):
        return self.nome_receita