from django.db import models

# Create your models here.
class Perfil(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nombre}"

class TipoLocal(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
       return f"{self.nombre}"

class Coordenadas(models.Model):
    latitud = models.CharField(max_length=500)
    longitud = models.CharField(max_length=500)
    def __str__(self):
        return f"{self.id}"

class TipoProducto(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nombre}"

class Locales(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.CharField(max_length=255)
    coordenadas = models.ForeignKey(Coordenadas, on_delete=models.CASCADE)
    tipo_local = models.ForeignKey(TipoLocal, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nombre}"
    
class Usuario(models.Model):
    usuario = models.CharField(max_length=50)
    contrasenna = models.CharField(max_length=50)
    correo = models.EmailField()
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.usuario}"
    
class Favorito(models.Model):
    local = models.ForeignKey(Locales, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Calificacion(models.Model):
    estrellas = models.IntegerField()
    comentario = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    local = models.ForeignKey(Locales, on_delete=models.CASCADE)

class Producto(models.Model):
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.CharField(max_length=255)
    tipo_producto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    local = models.ForeignKey(Locales, on_delete=models.CASCADE)