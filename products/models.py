from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class  Categoria(models.Model):
    name = models.CharField(max_length=40)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " by " + self.user.username


class SubCategoria(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(max_length=200)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return  self.categoria.name + "  " + self.name  

class Producto(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(max_length=200)
    sub_categoria = models.ForeignKey(SubCategoria,on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=0,max_digits=10)
    image = models.ImageField(upload_to="img/%y")
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " of " + self.sub_categoria.name
    