from django.forms import ModelForm
from .models import *

# Write down your form classes here.
class PartialCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']