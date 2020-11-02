from django.contrib import admin
from django_admin_row_actions import AdminRowActionsMixin
from .models import Cliente, Articulo, Pedido, Pedido_Articulo
# Register your models here.


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email',)
    list_filter = ('id', 'nombre', 'email')
    search_fields = ('nombre',)


@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio',)
    list_filter = ('id', 'nombre',)
    search_fields = ('nombre',)


# @admin.register(Pedido_Articulo)
# class Pedido_ArticuloAdmin(admin.ModelAdmin):
#     list_display = ('id',)
#     list_filter = ('id',)

class Pedido_ArticuloAdminInline(admin.StackedInline):
    model = Pedido_Articulo
    extra = 1

@admin.register(Pedido)
class PedidoAdmin(AdminRowActionsMixin, admin.ModelAdmin):
    list_display = ('id', 'cliente', 'fecha', 'total', 'enviado')
    list_filter = ('id', 'cliente', 'fecha')
    search_fields = ('cliente',)
    inlines = [Pedido_ArticuloAdminInline, ]
    actions = ['make_published', ]

    def get_row_actions(self, obj):
        row_actions = [
            {
                'label': 'Descargar csv',
                'action': 'descargar_csv',
                'enabled': True,
            },
            {
                'label': 'Enviar email',
                'action': 'enviarMail',
                'enabled': obj.enviado is False,
            },
        ]
        row_actions += super(PedidoAdmin, self).get_row_actions(obj)
        return row_actions