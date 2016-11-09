from rest_framework import serializers, viewsets
from ioteca_service_apps.eventos.models.evento import Evento


class EventoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Evento


class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
