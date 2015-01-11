from django.forms import ModelForm

from gifai.models import Gif


class GifForm(ModelForm):
    class Meta:
        model = Gif
        fields = ['title', 'source']
        # title = forms.CharField(label="Title", max_length=200)
    #url = forms.URLField(label="URL")
