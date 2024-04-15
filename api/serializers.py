from rest_framework import serializers
from .models import *

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'

class TipoLocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoLocal
        fields = '__all__'

class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = '__all__'

class CoordenadasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordenadas
        fields = '__all__'

class LocalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locales
        fields = '__all__'
        
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class FavoritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorito
        fields = '__all__'

class CalificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calificacion
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'