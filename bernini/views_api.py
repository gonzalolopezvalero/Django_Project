# from rest_framework.mixins import CreateModelMixin
# from rest_framework.generics import RetrieveAPIView
# from bernini.models import Articulo
# from bernini.serializers import ArticuloModelSerializer

# class ArticuloRetrieveAPIView(CreateModelMixin, RetrieveAPIView):
#     serializer_class = ArticuloModelSerializer
#     queryset = Articulo.objects.all()

#     def get_object(self):
#         queryset = self.filter_queryset(self.get_queryset())
#         # make sure to catch 404's below
#         obj = queryset.get(pk=self)
#         self.check_object_permissions(self.request, obj)
#         return obj

from bernini.models import Articulo
from rest_framework import viewsets
from bernini.serializers import ArticuloModelSerializer


class ArticuloViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Articulo.objects.all().order_by('id')
    serializer_class = ArticuloModelSerializer
