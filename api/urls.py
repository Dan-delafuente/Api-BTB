from rest_framework import routers
from .api import *

router = routers.DefaultRouter()

router.register('api/Perfil', PerfilViewSet, 'Perfil')
router.register('api/TipoLocal', TipoLocalViewSet, 'Tipo Local')
router.register('api/TipoProducto', TipoProductoViewSet, 'Tipo Producto')
router.register('api/Coordenadas', CoordenadasViewSet, 'Coordenadas')
router.register('api/Locales', LocalesViewSet, 'Locales')
router.register('api/Usuario', UsuarioViewSet, 'Usuario')
router.register('api/Favorito', FavoritoViewSet, 'Favorito')
router.register('api/Calificacion', CalificacionViewSet, 'Calificacion')
router.register('api/Producto', ProductoViewSet, 'Producto')

urlpatterns = router.urls