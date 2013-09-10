from django.db import models
from django.forms import ModelForm
<<<<<<< HEAD
from django.forms.widgets import TextInput
# Create your models here.
class metadata(models.Model):
    url=models.CharField(primary_key=True,max_length=100)
    title=models.CharField(null=True,max_length=200)
    meta_desc = models.CharField(null=True,max_length=1000)
    meta_keyw = models.CharField(null=True,max_length=1000)
=======
# Create your models here.
class metadata(models.Model):
    url=models.TextField(primary_key=True)
    title=models.TextField(null=True)
    meta_desc = models.TextField(null=True)
    meta_keyw = models.TextField(null=True)
>>>>>>> af723129d3705628ab69424b7cf40c0b7f5c7dba

class metadataform(ModelForm):
    class Meta:
        model=metadata
<<<<<<< HEAD
        fields={'url','title','meta_desc','meta_keyw'}   
        widgets = {    
                        'url': TextInput(attrs={'style': 'width:110px'}),
                        'title': TextInput(attrs={'style': 'width:170px'}),
                        'meta_desc': TextInput(attrs={'style': 'width:250px'}),
                        'meta_keyw': TextInput(attrs={'style': 'width:230px'})
                  }  
=======
        fields={'url','title','meta_desc','meta_keyw'}     
>>>>>>> af723129d3705628ab69424b7cf40c0b7f5c7dba
