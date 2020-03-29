from django.forms import ModelForm, ValidationError
from .models import *

# Write down your form classes here.
class PartialCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def clean(self):
        super().clean()
        data = self.cleaned_data
        if len(data['content']) > 500:
            raise ValidationError('Comment cannot be longer than 500 characters.')    

class PartialPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'post_image']

    def clean(self):
        super().clean()
        data = self.cleaned_data
        if len(data['content']) < 10:
            raise ValidationError('Post cannot be shorter than 10 characters.')    
        if len(data['title']) < 5 or len(data['title']) > 50:
            raise ValidationError('Post title must be between 5 and 50 characters.')