from django import forms
from .models import Post

class PostForm(forms.ModelForm):

	class Meta:
		#Tell django which model is to be used for the creation of the form
		model = Post
		#Tell django what fields will end be used in the form
		fields = ('title', 'text')
