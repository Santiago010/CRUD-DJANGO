from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm
from .models import Categoria,SubCategoria,Producto

class SubCategoryForm(ModelForm):
    name = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'p-2 rounded-md w-full my-1.5 bg-sky-50','placeholder':'Nombre...'}))
    description = forms.CharField(label='', widget=forms.Textarea(attrs={'class': "p-2 rounded-md w-full my-1.5 bg-sky-50",'placeholder': 'Descripción...'}))
    class Meta:
        model = SubCategoria
        fields = ['name','description','categoria']

        def __init__(self, *args, **kwargs):
            super(ProductForm, self).__init__(*args, **kwargs)
            # Obtener todas las subcategorias disponibles desde la base de datos
            categorias = Categoria.objects.all()
            # Crear una lista de tuplas con las opciones del campo 'sub_categoria'
            choices = [(categoria.id, categoria.name) for categoria in categorias]
            # Agregar las opciones al campo 'sub_categoria' del formulario
            self.fields['categoria'].widget = forms.Select(choices=choices) 

class CategoryForm(ModelForm):
    name = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'p-2 rounded-md w-full my-1.5 bg-sky-50','placeholder':'Nombre...'}))
    class Meta:
        model = Categoria
        fields = ['name']

class ProductForm(ModelForm):
    name = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'p-2 rounded-md w-full my-1.5 bg-sky-50','placeholder':'Nombre...'}))
    description = forms.CharField(label='', widget=forms.Textarea(attrs={'class': "p-2 rounded-md w-full my-1.5 bg-sky-50",'placeholder': 'Descripción...'}))
    price = forms.IntegerField(label='', widget=forms.NumberInput(attrs={'class': "p-2 rounded-md w-full my-1.5 bg-sky-50",'placeholder': 'precío...'}))

    class Meta:
        model = Producto
        fields = ['name', 'description', 'sub_categoria', 'price', 'image']
       
    
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        # Obtener todas las subcategorias disponibles desde la base de datos
        subcategorias = SubCategoria.objects.all()
        # Crear una lista de tuplas con las opciones del campo 'sub_categoria'
        choices = [(subcategoria.id, subcategoria.name) for subcategoria in subcategorias]
        # Agregar las opciones al campo 'sub_categoria' del formulario
        self.fields['sub_categoria'].widget = forms.Select(choices=choices)


class UserForm(UserCreationForm):
    first_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'p-2 rounded-md w-full my-1.5 bg-sky-50','placeholder':'Nombre...'}))
    last_name = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'p-2 rounded-md w-full my-1.5 bg-sky-50','placeholder':'Apellido...'}))
    email = forms.EmailField(label='',widget=forms.TextInput(attrs={'class': 'p-2 rounded-md w-full my-1.5 bg-sky-50','placeholder':'Correo...'}))
    username = forms.CharField(label='',widget=forms.TextInput(attrs={'class': 'p-2 rounded-md w-full my-1.5 bg-sky-50','placeholder':'Username...'}))
    password1 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class': 'p-2 rounded-md w-full my-1.5 bg-sky-50','placeholder':'Password1...'}))
    password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class': 'p-2 rounded-md w-full my-1.5 bg-sky-50','placeholder':'Password2...'}))

    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2' )

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomAuthenticationForm, self).__init__(*args, **kwargs)
        # Personalizar los atributos de los campos
        self.fields['username'].widget.attrs.update({
            'class': 'p-2 rounded-md w-full my-1.5 bg-sky-50',
            'placeholder': 'Username...',
        })
        self.fields['password'].widget.attrs.update({
            'class': 'p-2 rounded-md w-full my-1.5 bg-sky-50',
            'placeholder': 'Password...',
        })
        