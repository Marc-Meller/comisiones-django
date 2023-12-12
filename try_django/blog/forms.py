from django import forms
from .models import blogPost

class blogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea) 

class blogPostModelForm(forms.ModelForm):
    class Meta:
        model = blogPost
        fields = ['title', 'image', 'slug', 'content', 'publish_date']
        widgets = {
            'publish_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        
        
    def clean_title(self, *args, **kwargs):
        instance = self.instance
        title = self.cleaned_data.get('title')
        qs = blogPost.objects.filter(title__iexact=title)
        print(title)
        if instance is not (None):
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("El titulo ya ha sido utilizado, escriba otro.")
        return title