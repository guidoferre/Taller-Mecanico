from django import forms

class clienteFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    vehiculo = forms.CharField()





    