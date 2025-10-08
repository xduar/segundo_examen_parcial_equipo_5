# importar el método path
from django.urls import path
# importar las vistas
from .views import (
    # Producto
    ProductoListView,
    ProductoCreateView,
    ProductoDetailView,
    ProductoUpdateView,
    ProductoDeleteView,
    # Categoria
    CategoriaListView,
    CategoriaCreateView,
    # Proveedor
    ProveedorListView,
    ProveedorCreateView
    
)

# nombre descriptivo para las url
app_name = "productos"

# crear el enrutamiento de las url
urlpatterns = [
    # producto
    path('', ProductoListView.as_view(), name="producto-list"),
    path('producto/nuevo/', ProductoCreateView.as_view(), name="producto-create"),
    path('producto/<int:pk>/', ProductoDetailView.as_view(), name="producto-detail"),
    path('producto/<int:pk>/editar/', ProductoUpdateView.as_view(), name="producto-update"),
    path('producto/<int:pk>/eliminar/', ProductoDeleteView.as_view(), name="producto-delete"),
    # categoria
    path('categorias/', CategoriaListView.as_view(), name="categoria-list"),
    path('categorias/nuevo', CategoriaCreateView.as_view(), name="categoria-create"),
    # proveedor
    path('proveedores/', ProveedorListView.as_view(), name="proveedor-list"),
    path('proveedores/nuevo', ProveedorCreateView.as_view(), name="proveedor-form")
]