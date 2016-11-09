from django.db import models
from ioteca_service_apps.eventos.choices.montos import PAGO_INASISTENCIA_CHOICES
from ioteca_service_apps.asociacion.models.lote import Lote
from .evento import Evento, TimeStampModel


class Inasistencia(TimeStampModel):

    evento = models.ForeignKey(Evento)
    socio = models.ForeignKey(Lote)
    monto = models.CharField(max_length=2, choices=PAGO_INASISTENCIA_CHOICES)
    num_inasistencias = models.IntegerField()

    class Meta:
        verbose_name = "Inasistencia"
        verbose_name_plural = "Inasistencias"

    def __str__(self):
        return ""
