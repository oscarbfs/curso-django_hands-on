from django.contrib.auth import get_user_model
from django.db import models


class Canal(models.Model):
    nome = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    inicio = models.DateField()
    fim = models.DateField()
    usuarios = models.ManyToManyField(get_user_model(), through='Inscricao')


class Inscricao(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    canal = models.ForeignKey(Canal, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['usuario', 'canal']]
        ordering = ['canal', 'data']
