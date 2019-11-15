# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Adjust
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Categorias(models.Model):
    idcategoria = models.IntegerField(db_column='idCategoria', primary_key=True)  # Field name made lowercase.
    nombrecategoria = models.CharField(db_column='nombreCategoria', unique=True, max_length=15)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', unique=True, max_length=255, blank=True, null=True)  # Field name made lowercase.
    imagen = models.CharField(db_column='Imagen', unique=True, max_length=45, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
            return self.nombrecategoria

    class Meta:
        #managed = False
        db_table = 'Categorias'


class Clientes(models.Model):
    idcliente = models.IntegerField(db_column='idCliente', primary_key=True)  # Field name made lowercase.
    nombrecontacto = models.CharField(db_column='NombreContacto', max_length=45)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=45)  # Field name made lowercase.
    ciudad = models.CharField(db_column='Ciudad', max_length=15)  # Field name made lowercase.
    localidad = models.CharField(db_column='Localidad', max_length=15)  # Field name made lowercase.
    codpostal = models.CharField(db_column='CodPostal', max_length=10)  # Field name made lowercase.
    pais = models.CharField(db_column='Pais', max_length=15)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', unique=True, max_length=15)  # Field name made lowercase.
    e_mail = models.CharField(db_column='e-mail', unique=True, max_length=45)  # Field renamed to remove unsuitable characters.
    password = models.CharField(db_column='Password', unique=True, max_length=15)  # Field name made lowercase.

    def __str__(self):
            return self.e_mail

    class Meta:
        #managed = False
        db_table = 'Clientes'


class Companiasdeenvios(models.Model):
    idcompañiasdeenvio = models.IntegerField(db_column='idCompañiasDeEnvio', primary_key=True)  # Field name made lowercase.
    nombrecompañia = models.CharField(db_column='NombreCompañia', unique=True, max_length=20)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', unique=True, max_length=15)  # Field name made lowercase.
    e_mail = models.CharField(db_column='e-mail', unique=True, max_length=45)  # Field renamed to remove unsuitable characters.

    def __str__(self):
            return self.nombrecompañia

    class Meta:
        #managed = False
        db_table = 'CompañiasDeEnvios'


class Pedidos(models.Model):
    idpedido = models.IntegerField(db_column='idPedido', primary_key=True)  # Field name made lowercase.
    fechapedido = models.DateField(db_column='FechaPedido')  # Field name made lowercase.
    fechaentrega = models.DateField(db_column='FechaEntrega', blank=True, null=True)  # Field name made lowercase.
    fechaenvio = models.DateField(db_column='FechaEnvio', blank=True, null=True)  # Field name made lowercase.
    monto = models.FloatField(db_column='Monto')  # Field name made lowercase.
    destinatario = models.CharField(db_column='Destinatario', max_length=30)  # Field name made lowercase.
    direcciondestinatario = models.CharField(db_column='DireccionDestinatario', max_length=45)  # Field name made lowercase.
    ciudaddestinatario = models.CharField(db_column='CiudadDestinatario', max_length=15)  # Field name made lowercase.
    localidaddestinatario = models.CharField(db_column='LocalidadDestinatario', max_length=20)  # Field name made lowercase.
    codpostaldestinatario = models.CharField(db_column='CodPostalDestinatario', max_length=10)  # Field name made lowercase.
    paisdestinatario = models.CharField(db_column='PaisDestinatario', max_length=15)  # Field name made lowercase.
    idcompañiasdeenvio = models.ForeignKey(Companiasdeenvios, models.PROTECT, db_column='IdCompañiasDeEnvio')  # Field name made lowercase.
    idcliente = models.ForeignKey(Clientes, models.PROTECT, db_column='idCliente')  # Field name made lowercase.
    
    pago_estado = (
        ('a', 'Aprovado'),
        ('p', 'Pendiente'),
        ('r', 'Rechazado'),
    )
    estadopago = models.CharField(db_column='EstadoPago', max_length=1, choices=pago_estado)  # Field name made lowercase.

    pago_forma = (
        ('e', 'Efectivo'),
        ('d', 'Depósito'),
    )
    formapago = models.CharField(db_column='FormaPago', max_length=1, choices=pago_forma)  # Field name made lowercase.

    def __str__(self):
            return str(self.idpedido) + " / " + str(self.idcliente) + " / " + self.destinatario

    class Meta:
        #managed = False
        db_table = 'Pedidos'


class Proveedores(models.Model):
    idproveedor = models.IntegerField(db_column='idProveedor', primary_key=True)  # Field name made lowercase.
    nombrecompañia = models.CharField(db_column='NombreCompañia', unique=True, max_length=20)  # Field name made lowercase.
    nombrecontacto = models.CharField(db_column='NombreContacto', max_length=45)  # Field name made lowercase.
    cargocontacto = models.CharField(db_column='CargoContacto', max_length=15)  # Field name made lowercase.
    direccion = models.CharField(db_column='Direccion', max_length=45)  # Field name made lowercase.
    ciudad = models.CharField(db_column='Ciudad', max_length=15)  # Field name made lowercase.
    localidad = models.CharField(db_column='Localidad', max_length=15)  # Field name made lowercase.
    codpostal = models.CharField(db_column='CodPostal', max_length=10)  # Field name made lowercase.
    pais = models.CharField(db_column='Pais', max_length=15)  # Field name made lowercase.
    telefono = models.CharField(db_column='Telefono', unique=True, max_length=15)  # Field name made lowercase.
    e_mail = models.CharField(db_column='e-mail', unique=True, max_length=45)  # Field renamed to remove unsuitable characters.
    paginaprincipal = models.CharField(db_column='PaginaPrincipal', unique=True, max_length=30, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
            return self.nombrecompañia

    class Meta:
        #managed = False
        db_table = 'Proveedores'


class Productos(models.Model):
    idproducto = models.IntegerField(db_column='idProducto', primary_key=True)  # Field name made lowercase.
    nombreproducto = models.CharField(db_column='NombreProducto', unique=True, max_length=45)  # Field name made lowercase.
    cantidadporunidad = models.IntegerField(db_column='CantidadPorUnidad')  # Field name made lowercase.
    preciounidad = models.FloatField(db_column='PrecioUnidad')  # Field name made lowercase.
    unidadesenexistencia = models.IntegerField(db_column='UnidadesEnExistencia')  # Field name made lowercase.
    unidadesenpedido = models.IntegerField(db_column='UnidadesEnPedido')  # Field name made lowercase.
    
    demanda_nivel = (
        ('b', 'Bajo'),
        ('m', 'Medio'),
        ('a', 'Alto'),
    )
    demanda = models.CharField(db_column='Demanda', max_length=1, choices=demanda_nivel)  # Field name made lowercase.
    
    es_suspendido = (
        ('s','Sí'),
        ('n','No'),
    )
    suspendido = models.CharField(db_column='Suspendido', max_length=1, choices=es_suspendido)  # Field name made lowercase.
    
    idproveedor = models.ForeignKey(Proveedores, models.PROTECT, db_column='IdProveedor')  # Field name made lowercase.
    idcategoria = models.ForeignKey(Categorias, models.PROTECT, db_column='idCategoria')  # Field name made lowercase.
    imagen = models.CharField(db_column='Imagen', unique=True, max_length=45)  # Field name made lowercase.
    imagentest = models.ImageField(upload_to='img_prod', null=True, blank=True)
    thumbnail = ImageSpecField([Adjust(contrast=1.2, sharpness=1.1),
                ResizeToFill(50, 50)], source='imagentest',
                format='JPEG', options={'quality': 90})

    def __str__(self):
            return self.nombreproducto

    def get_absolute_url(self):
            """
            Devuelve el URL a una instancia particular de Productos
            """
            return reverse('product-detail', args=[str(self.idproducto)])

    class Meta:
        #managed = False
        db_table = 'Productos'


class Detallesdepedidos(models.Model):
    idpedido = models.ForeignKey(Pedidos, models.PROTECT, db_column='IdPedido', primary_key=True)  # Field name made lowercase.
    idproducto = models.ForeignKey(Productos, models.PROTECT, db_column='IdProducto')  # Field name made lowercase.
    preciounidad = models.FloatField(db_column='PrecioUnidad')  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad')  # Field name made lowercase.
    descuento = models.FloatField(db_column='Descuento', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
            return "(" + str(self.idpedido) + ") / " + str(self.idproducto)

    class Meta:
        #managed = False
        db_table = 'DetallesDePedidos'
        unique_together = (('idpedido', 'idproducto'),)
