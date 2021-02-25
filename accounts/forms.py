from django import forms
from .models import User, Profile
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from rest_framework.authtoken.models import Token


class UserCreationForm(forms.ModelForm):
    email = forms.EmailField(label = 'Email', widget = forms.EmailInput(attrs = {'class':'form-control mb-3'}))
    full_name = forms.CharField(label = 'Full Name', widget = forms.TextInput(attrs = {'class':'form-control mb-3'}))
    password1 = forms.CharField(label = 'Password', widget=forms.PasswordInput(attrs = {'class':'form-control mb-3'}))
    password2 = forms.CharField(label = 'Confirm password', widget=forms.PasswordInput(attrs = {'class':'form-control '}))
    
    class Meta:
        model = User
        fields = ('email', 'full_name')
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise forms.ValidationError("Passwords don't match")
        return cd['password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'full_name')

    def clean_password(self):
        return self.initial["password"]

class UserLoginForm(forms.Form):
    email = forms.EmailField(label = 'Email', widget = forms.EmailInput(attrs = {'class':'form-control'}))
    password = forms.CharField(label = 'Password', widget = forms.PasswordInput(attrs = {'class':'form-control'}))

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','full_name','password1','password2')


class UserinfoSettingsForm(forms.ModelForm):
    email = forms.EmailField(label = 'Email', widget = forms.EmailInput(attrs = {'class':'form-control mb-3'}))
    full_name = forms.CharField(label = 'Full Name', widget = forms.TextInput(attrs = {'class':'form-control mb-3'}))
    
    class Meta:
        model = User
        fields = ('email', 'full_name')

class ProfileSettingsForm(forms.ModelForm):
    avatar = forms.FileField(label = 'Avatar',
                            required=False, 
                            error_messages = {'invalid': "Image files only" }, 
                            widget = forms.FileInput(
                                                    attrs = {'id':'id_avatar','class':'clearablefileinput form-control mb-3'})
                                                    )

    class Meta:
        model = Profile
        fields = ('avatar',)
