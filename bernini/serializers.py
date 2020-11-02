from rest_framework import serializers, viewsets

from bernini.models import Articulo


class ArticuloModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = (
            'id',
            'nombre',
            'precio'
        )
