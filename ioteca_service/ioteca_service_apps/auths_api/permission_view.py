from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from django.db.models import Q
from functools import reduce
from operator import __or__ as OR
import json

from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from rest_framework import serializers, viewsets

from ioteca_service_apps.utils.pagination import ModelPagination
from ioteca_service_apps.utils.security import log_params
from ioteca_service_apps.utils.permissions import ModelPermission


class ContentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContentType


class PermissionSerializer(serializers.ModelSerializer):
    content_type = ContentTypeSerializer(
        required=False, many=False, read_only=True)

    class Meta:
        model = Permission


class PermissionViewSet(ModelPagination, viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    # pagination_class = LimitOffsetPagination
