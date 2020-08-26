from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

from openhouce.base import response
from openhouce.base.api.mixins import MultipleSerializerMixin
from openhouce.urlshotener import serializer
from openhouce.urlshotener.services import create_shortenurl


class ShortURLViewSet(MultipleSerializerMixin, viewsets.GenericViewSet):
    permission_class = [AllowAny, ]

    serializer_classes = {
        'generate_url': serializer.ShortURLSerializer
    }

    @action(methods=['POST'], detail=False)
    def generate_url(self, request):
        serializer_data = self.get_serializer(data=request.data)
        serializer_data.is_valid(raise_exception=True)
        data = create_shortenurl(**serializer_data.validated_data)
        data = serializer.ShortURLDisplaySerializer(data).data
        return response.Created(data)
