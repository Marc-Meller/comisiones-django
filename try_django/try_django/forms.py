from django import forms

class contactForm(forms.Form):
    full_name = forms.CharField(label='Nombre completo')
    email = forms.EmailField(label='Correo electrónico')
    content = forms.CharField(widget=forms.Textarea, label='Mensaje')
    
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        print(email)
        if email.endswith(".edu"):
            raise forms.ValidationError("Esta direccion de correo no es valida. No utilice .edu.")
        return email