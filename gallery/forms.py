from django import forms
from .models import Image
# import gettext lazy function
from django.utils.translation import gettext_lazy as _

class ImageForm(forms.ModelForm):
    title = forms.CharField(
        label=_('Title'),
        max_length=100,
        required=True,
    )    
    
    description = forms.CharField(
        label=_('Description'),
        widget=forms.Textarea,
        required=False,
    )
    
    image = forms.ImageField(
        label=_('Image'),
        required=True,
    )
    
    class Meta:
        model = Image
        fields = ['title', 'description', 'image']
