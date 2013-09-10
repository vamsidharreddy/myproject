from django.db import models
from django.forms import ModelForm
# Create your models here.
class metadata(models.Model):
    url=models.TextField(primary_key=True)
    title=models.TextField(null=True)
    meta_desc = models.TextField(null=True)
    meta_keyw = models.TextField(null=True)

class metadataform(ModelForm):
    class Meta:
        model=metadata
        fields={'url','title','meta_desc','meta_keyw'}     
