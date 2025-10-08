from django.db import models

# Create your models here.

# importar la clase Model de models.

# Sistema de Inventario Completo
class Categoria(models.Model):
    
    # crear los atributos
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(null=True, blank=True)
    
    # ajustar la tabla
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["nombre"]

class Proveedor(models.Model):
    
    # crear los atributos
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)
    contacto = models.CharField(max_length=100, null=True, blank=True)
    
    # ajustar la tabla
    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"
        ordering = ["nombre"]
    
    
# create table Producto()
class Producto(models.Model): # aplicando herencia

    # crear los atributos
    nombre = models.CharField(max_length=50) # nombre varchar(50) not null
    descripcion = models.TextField(null=True, max_length=150) # descripcion varchar(150)
    precio_compra = models.DecimalField(max_digits=12, decimal_places=2) # precio decimal(12,2) not null
    precio_venta = models.DecimalField(max_digits=12, decimal_places=2) # precio decimal(12,2) not null
    stock = models.IntegerField(default=0)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)


    # crear un metodo
    def __str__(self): # polimorfismo
        return f"{self.nombre} - {getattr(self, 'stock', 0)} unidades"
