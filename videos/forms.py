from django import forms
from django.db import models
from django.forms import ModelForm
from django import forms
from django.db.models import fields
from videos.models import Video
from django.db.models import CharField, DateField, ForeignKey, Model
from . import models
from autoslug import AutoSlugField

# class postform(forms.Form):

#     video = forms.FileField()
    
    
def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


class postform(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('title','body','video')

        
        