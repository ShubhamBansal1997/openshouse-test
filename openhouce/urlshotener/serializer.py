from rest_framework import serializers

from openhouce.urlshotener.models import ShortURL


class ShortURLSerializer(serializers.Serializer):
    url = serializers.CharField(allow_blank=False, trim_whitespace=True)


class ShortURLDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURL
        fields = '__all__'
