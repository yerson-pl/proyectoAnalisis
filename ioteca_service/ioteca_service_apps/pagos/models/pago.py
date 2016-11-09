from django.db import models
from ioteca_service_apps.eventos.models.inasistencia import Inasistencia
from .periodo import Periodo
from ioteca_service_apps.eventos.models.evento import TimeStampModel


class Pago(TimeStampModel):

    inasistencia = models.ForeignKey(Inasistencia)
    periodo = models.ForeignKey(Periodo)
    imagen = models.ImageField()
    monto = models.DecimalField(decimal_places=2, max_digits=5)
    num_recibo = models.CharField(max_length=50)
    validacion = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"

    def __str__(self):
        return ""