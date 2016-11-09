from django.conf.urls import url, include
from rest_framework import routers

from .inasistencia_view import InasistenciaViewSet
from .evento_view import EventoViewSet
from .asistencia_view import AsistenciaViewSet

router = routers.DefaultRouter()

router.register(r'inasistencias', InasistenciaViewSet)
router.register(r'eventos', EventoViewSet, 'eventos-view')
router.register(r'asistencias', AsistenciaViewSet, 'asistencia-view')

urlpatterns = [

    url(r'^', include(router.urls)),

]