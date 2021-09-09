from django import forms
from . models import BlogModel

class PostForm(forms.ModelForm):
    class Meta:
        model=BlogModel
        fields=('title_tag','title','author','image','description')

        widgets={
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'hidden'}),
            'image':forms.FileInput(attrs={'class':'form-control-file'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
        }



class UpdateForm(forms.ModelForm):
    class Meta:
        model=BlogModel
        fields=('title_tag','title','image','description')

        widgets={
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control-file'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),

        }