from rest_framework import serializers, viewsets
from ioteca_service_apps.eventos.models.asistencia import Asistencia


class AsistenciaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Asistencia
       

class AsistenciaViewSet(viewsets.ModelViewSet):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSerializer