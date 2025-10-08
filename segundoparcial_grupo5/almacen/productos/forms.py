from django import forms
from .models import Categoria, Proveedor
from .models import Producto

# crear un formulario personalizado para las Categorias
class CategoriaForm(forms.ModelForm):
    # ajuste al formulario generico
    class Meta:
        model = Categoria
        fields = ["nombre", "descripcion"]
        widgets = {
            "nombre": forms.TextInput(attrs={ "class": "form-control", "placeholder": "Nombre de la Categoria"}),
            "descripcion": forms.Textarea(attrs={ "class": "form-control", "placeholder": "Descripción de la Categoria", "rows": 3 })
        }
        
# crear un formulario personalizado para los proveedores
class ProveedorForm(forms.ModelForm):
    # ajustes al formulario
    class Meta:
        model = Proveedor
        fields = ["nombre", "telefono", "email", "direccion", "contacto"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre del Proveedor"}),
            "telefono": forms.TextInput(attrs={"class": "form-control", "placeholder": "70544596", "type": "cel"}),
            "email": forms.TextInput(attrs={"class": "form-control", "placeholder": "alguien@example.com", "type": "email"}),
            "direccion": forms.Textarea(attrs={"class": "form-control", "placeholder": "Direccion del proveedor", "rows": 3 }),
            "contacto": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre del Contacto"}),
        }


# Formulario para Producto
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["nombre", "descripcion", "precio_compra", "precio_venta", "stock", "activo", "categoria", "proveedor"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nombre del producto"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "precio_compra": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "precio_venta": forms.NumberInput(attrs={"class": "form-control", "step": "0.01"}),
            "stock": forms.NumberInput(attrs={"class": "form-control", "min": 0}),
            "activo": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "categoria": forms.Select(attrs={"class": "form-select"}),
            "proveedor": forms.Select(attrs={"class": "form-select"}),
        }

    def clean_precio_compra(self):
        precio_compra = self.cleaned_data.get('precio_compra')
        if precio_compra is None:
            return precio_compra
        if precio_compra < 0:
            raise forms.ValidationError('El precio de compra no puede ser negativo')
        return precio_compra

    def clean_precio_venta(self):
        precio_venta = self.cleaned_data.get('precio_venta')
        if precio_venta is None:
            return precio_venta
        if precio_venta < 0:
            raise forms.ValidationError('El precio de venta no puede ser negativo')
        return precio_venta

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock is None:
            return stock
        if stock < 0:
            raise forms.ValidationError('El stock no puede ser negativo')
        return stock

    def clean(self):
        cleaned = super().clean()
        precio_compra = cleaned.get('precio_compra')
        precio_venta = cleaned.get('precio_venta')
        if precio_compra is not None and precio_venta is not None:
            if precio_venta < precio_compra:
                raise forms.ValidationError('El precio de venta debe ser mayor o igual al precio de compra')
        return cleaned