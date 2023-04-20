from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'control', 'placeholder':'Enter your title'}))

    class  Meta():
        model = Post
        fields = ('title', 'content')