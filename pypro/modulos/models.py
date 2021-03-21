from django.db import models


class Modulo(models.Model):
    titulo = models.Charfield(max_lenght=64)
