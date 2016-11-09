from rest_framework import serializers, viewsets
from ioteca_service_apps.eventos.models.inasistencia import Inasistencia

class InasistenciaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inasistencia


class InasistenciaViewSet(viewsets.ModelViewSet):
    queryset = Inasistencia.objects.all()
    serializer_class = InasistenciaSerializer
