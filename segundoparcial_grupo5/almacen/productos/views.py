from django.shortcuts import render
# importar vistas genericas
from django.views.generic import ListView, CreateView
from django.views.generic import DetailView, UpdateView, DeleteView
# importar las clases
from .models import Producto, Categoria, Proveedor
# importar método reverse_lazy
from django.urls import reverse_lazy
# importar los formularios personalizados
from .forms import CategoriaForm, ProveedorForm
from .forms import ProductoForm
from django.urls import reverse_lazy

# Create your views here.

# crear una clase generica para mostrar el listado de productos
class ProductoListView(ListView):
    
    # Indicar el modelo base
    model = Producto
    # Indicamos el template (plantilla)
    template_name = "producto/producto-list.html"
    # nombre del contexto del objetos
    context_object_name = "productos"
    
    
# crear una clase generica para mostrar el listado de categorias
class CategoriaListView(ListView):
    
    model = Categoria
    template_name = "categoria/categoria-list.html"
    context_object_name = "categorias"

# crear una clase generica para guardar una nueva categoria
class CategoriaCreateView(CreateView):
    
    model = Categoria
    form_class = CategoriaForm
    template_name = "categoria/categoria-form.html"
    success_url = reverse_lazy("productos:categoria-list")
    
    
# crear una clase generica para mostrar el listado de proveedor
class ProveedorListView(ListView):
    
    model = Proveedor
    template_name = "proveedor/proveedor-list.html"
    context_object_name = "proveedores"

# crear una clase generica para guardar un nuevo proveedor
class ProveedorCreateView(CreateView):
    
    model = Proveedor
    form_class = ProveedorForm
    template_name = "proveedor/proveedor-form.html"
    success_url = reverse_lazy("productos:proveedor-list")


# Vistas CRUD para Producto
class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = "producto/producto-form.html"
    success_url = reverse_lazy("productos:producto-list")


class ProductoDetailView(DetailView):
    model = Producto
    template_name = "producto/producto-detail.html"
    context_object_name = "producto"


class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = "producto/producto-form.html"
    success_url = reverse_lazy("productos:producto-list")


class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "producto/producto-delete.html"
    success_url = reverse_lazy("productos:producto-list")
