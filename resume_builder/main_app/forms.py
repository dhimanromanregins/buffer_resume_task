from django import forms
from .models import Profile
from django.core.exceptions import ValidationError


def validate_username(name):
    if len(name) < 3:
        raise ValidationError(('Username must be at least 4 characters long.'),
            code='invalid_username'
        )

def validate_phone_number(phone_number):
    if not phone_number.isdigit():
        raise ValidationError(
            ('Phone number must contain only digits.'),
            code='invalid_phone_number'
        )
    if len(phone_number) != 10:
        raise ValidationError(
            ('Phone number must be 10 digits.'),
            code='invalid_phone_number'
        )

def validate_email(email):
    from django.core.validators import validate_email
    from django.core.exceptions import ValidationError
    try:
        validate_email(email)
    except ValidationError:
        raise ValidationError(
            ('Invalid email address.'),
            code='invalid_email'
        )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'phone', 'school', 'degree', 'university', 'skill', 'about_you', 'previous_projects']



    def clean_name(self):
        name = self.cleaned_data['name']
        validate_username(name)
        return name

    def clean_email(self):
        email = self.cleaned_data['email']
        if Profile.objects.filter(email=email).exists():
            raise forms.ValidationError("Email address already exists.")
        validate_email(email)
        return email

    def clean_phone_number(self):
        phone = self.cleaned_data['phone']
        validate_phone_number(phone)
        return phone



