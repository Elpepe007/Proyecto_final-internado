from django import forms

class formulario_internos(forms.Form):
    
    nombre=forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    trabajo=forms.CharField(max_length=40)
    horas_de_trabajo = forms.IntegerField()