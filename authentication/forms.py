from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.utils.safestring import SafeString
from . import validators



class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom d’utilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')
    
    
class SignupForm(UserCreationForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     # for field in self.fields:
    #     #     field.widget.attrs.update({"class": "form-control"})
    #     print(self.fields["username"].widget)
    #     self.fields["username"].widget.attrs.update({"class": "form-control"})
    #     # self.fields["comment"].widget.attrs.update(size="40")
        
    def as_p(self):
        return SafeString(super().as_div().replace("<p>", "<p class='form-group'>"))
    
    def as_div(self):
        return SafeString(super().as_div().replace("<div>", "<div class='form-group'>"))

        
    class Meta(UserCreationForm.Meta):
        model =get_user_model()
        fields = ('username','email','first_name','last_name','role')
           
        
class PostCodeForm(forms.Form):
    post_code = forms.CharField(max_length=10, validators=[validators.PostCodeValidator])