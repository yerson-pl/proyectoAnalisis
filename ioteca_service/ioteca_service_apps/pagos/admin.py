from django.contrib import admin

from .models.pago import Pago
from .models.periodo import Periodo

admin.site.register(Pago)
admin.site.register(Periodo)
