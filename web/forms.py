from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(
        max_length=50,
        label= 'Nombre:',
        widget=forms.TextInput (attrs={
            'class': 'form-control mb-3 fst-italic',
            'placeholder': 'Ingrese nombre aqui'
        })
    )
    email = forms.EmailField(
        max_length=100,
        label= 'Email:',
        widget=forms.EmailInput(attrs={
            'class': 'form-control mb-3 fst-italic',
            'placeholder': 'Ingrese su correo aqui'
        })
    )
    mensaje = forms.CharField(
        label='Mensaje:',
        max_length=500,
        widget=forms.Textarea (attrs={
            'class': 'form-control mb-3 fst-italic',
            'rows': 5,
            'placeholder': 'Ingrese su mensaje, maximo 500 caracteres'
        })
    )
    
    
    
    
    