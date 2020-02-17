from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

class SignupForm(ModelForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailField(
            attrs={
                'class':'form-control',
                'placeholder':'email',
                'required': 'true',
            }
        )
    )

    verify_password = forms.CharField(label='비밀번호 확인', widget=forms.PasswordInput)

    field_order = [
        'username', 'email', 'password', 'verify_password', 'phone'
    ]

    class Meta:
        model = User
        widget = {'password':forms.PasswordInput}
        fields = ['username', 'email', 'password', 'verify_password', 'phone']

    def clean_verify_password(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('verify_password')
        if password1 != password2:
            raise forms.ValidationError('Error')
        return password2
