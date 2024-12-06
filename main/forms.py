from django import forms
from .models import Product, CustomUser

class SignInForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

class BaseSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data

class SignUpForm(BaseSignUpForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'genre']

class BuyerSignUpForm(BaseSignUpForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

class SellerSignUpForm(BaseSignUpForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
