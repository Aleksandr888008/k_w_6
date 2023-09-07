from  django import forms

from blog.models import Blog
from mailing.forms import FormStyleMixin


class BlogForm(FormStyleMixin, forms.ModelForm):

    class Meta:
        model = Blog
        fields = '__all__'
