from django.contrib import admin
from imagekit.admin import AdminThumbnail
from .models import Categorias, Clientes, Companiasdeenvios, Pedidos, Proveedores, Productos, Detallesdepedidos 
# Register your models here.

admin.site.register(Categorias)
admin.site.register(Clientes)
admin.site.register(Companiasdeenvios)
admin.site.register(Pedidos)
admin.site.register(Proveedores)

#admin.site.register(Productos)
class ProductosAdmin(admin.ModelAdmin):

	list_display = ('image_display','idproducto', 'nombreproducto', 'preciounidad')
	image_display = AdminThumbnail(image_field='thumbnail')
	image_display.short_description = 'Image'
	readonly_fields = ['image_display']

admin.site.register(Productos, ProductosAdmin)

admin.site.register(Detallesdepedidos)