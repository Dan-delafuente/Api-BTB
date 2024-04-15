from .models import *
from rest_framework import viewsets, permissions
from .serializers import *

class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PerfilSerializer

class TipoLocalViewSet(viewsets.ModelViewSet):
    queryset = TipoLocal.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipoLocalSerializer

class TipoProductoViewSet(viewsets.ModelViewSet):
    queryset = TipoProducto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TipoProductoSerializer

class CoordenadasViewSet(viewsets.ModelViewSet):
    queryset = Coordenadas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CoordenadasSerializer

class LocalesViewSet(viewsets.ModelViewSet):
    queryset = Locales.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LocalesSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuarioSerializer

class FavoritoViewSet(viewsets.ModelViewSet):
    queryset = Favorito.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = FavoritoSerializer

class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CalificacionSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializer