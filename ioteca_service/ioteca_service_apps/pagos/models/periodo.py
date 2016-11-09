from django.db import models


class Periodo(models.Model):

    estado = models.BooleanField(default=False)
    nombre = models.CharField(max_length=50, default='')

    class Meta:
        verbose_name = "Periodo"
        verbose_name_plural = "Periodos"

    def __str__(self):
        return '%s' % (self.fecha)
