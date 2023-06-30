from django.db import models
from django.forms import PasswordInput

# Create your models here.
class Usuarios(models.Model):
    name:models.CharField(max_length=30)
    email:models.EmailField(max_length=50)
    password:models.CharField(PasswordInput)
    confirmpassword: models.CharField(PasswordInput)