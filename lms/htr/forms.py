from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from .models import CustomUser, UserProfile  # Adjust this import based on your app structure

# Use get_user_model() to fetch the User model dynamically
User = get_user_model()

# Update CustomUserCreationForm in forms.py
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2')

        
class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')       

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'phone_number', 'discord')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_photo', 'facebook', 'twitter', 'linkedin', 'instagram']

# Update UserLoginForm in forms.py
class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            user = authenticate(username=email, password=password)
            if not user:
                raise forms.ValidationError('Invalid email or password.')
        return cleaned_data



class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'