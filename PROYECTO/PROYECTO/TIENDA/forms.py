from django import forms
from .models import Producto


class FormProductoCustom(forms.ModelForm):

    # campos del modelo
    class Meta:
        model = Producto
        fields = ('titulo', 'categoria', 'precio',
                  'descripcion_producto', 'imagen')
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'titulo-pr'}),
            'precio': forms.TextInput(attrs={'class': 'precio-pr'}),
            'descripcion_producto': forms.Textarea(attrs={'class': 'descripcion-pr', 'id': 'id_descripcion'}),
            'imagen': forms.FileInput(attrs={'name': 'imagen_adjunta', 'class': 'imagen-pr'}),
        }
