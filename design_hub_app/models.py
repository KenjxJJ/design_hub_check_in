from django.db import models
from django.forms import ModelForm
from django.shortcuts import redirect


# Create your models here.
class Visitor(models.Model):
    name = models.CharField(max_length=55)
    temperature = models.DecimalField(max_digits=3,decimal_places=1) 
    company = models.CharField(max_length=95)
    id_number = models.CharField(max_length=12, blank=True)
    telephone_number = models.CharField(max_length=15)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

#  Add a new visitor
class VisitorForm(ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Visitor
        exclude = ['id']
