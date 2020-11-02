from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.fields import AutoSlugField
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from urllib.parse import urlparse
import csv
from io import StringIO
# Create your models here.


class Cliente(models.Model):
    nombre = models.CharField(verbose_name=_('Name'), max_length=50)
    email = models.CharField(verbose_name=_('Email'), max_length=50)

    def __str__(self):
            return self.nombre

class Articulo(models.Model):
    nombre = models.CharField(verbose_name=_('Name'), max_length=50)
    precio = models.FloatField(verbose_name=_('Precio'), default=0)

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField(verbose_name=_('Fecha'))
    enviado = models.BooleanField(verbose_name=_("Enviado"), default=False)

    def __str__(self):
        return '{}-{}-{}'.format(self.id, self.cliente.nombre, self.fecha)

    @property
    def total(self):
        total = 0
        for item in self.pedido_articulo.all():
            total += item.precio_cantidad
        return total
    
    def csv(self):
        articulos = self.pedido_articulo.all()

        with StringIO() as string_csv:
            f = csv.writer(string_csv, delimiter=';')

            f.writerow(
                ['', 'Articulo ID', 'Nombre', 'Cantidad', 'Precio', 'Total'],
            )

            for position, item in enumerate(articulos, start=1):
                f.writerow(
                    [position, item.articulo.id, item.articulo.nombre, item.cantidad, item.articulo.precio, item.precio_cantidad]
                )

            f.writerow(
                ['', '', '', '', 'TOTAL', self.total],
            )

            return string_csv.getvalue()

    def descargar_csv(self):
        return HttpResponse(self.csv(), content_type='text/csv')

    def enviarMail(self):
        """ Solo faltaria poner una función para mandar el mail 
            utilizando la libreria from django.core.mail import EmailMessage
            Entiendo que no hace falta implementar el caso de uso."""

        self.enviado = True
        self.save()


class Pedido_Articulo(models.Model):
    articulo = models.ForeignKey(Articulo, verbose_name=_('Articulo'), related_name='pedido_articulo', on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(verbose_name=_('Cantidad'), default=0)
    pedido = models.ForeignKey(Pedido, verbose_name=_('Articulo'), related_name='pedido_articulo',
                                null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.articulo.nombre

    @property
    def precio_cantidad(self):
        return self.articulo.precio * self.cantidad