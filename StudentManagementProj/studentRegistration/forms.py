from django import forms
from .models import StudentRegistration

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = StudentRegistration
        fields = ['st_name', 'email', 'mobile_no', 'profile_image', 'date_of_birth'] # type: ignore

        widgets = {
                'st_name': forms.TextInput
                (attrs={
                    'class': 'form-control mb-2', 
                    'placeholder':"Name ...", 
                    'id': "st_name_id",
                    'name': 'st_name'
                    }),
                'email': forms.EmailInput(attrs={
                    'class':"form-control mb-2",
                    'id':"email_id",
                    'name':"email",
                    'placeholder':"Email ..."
                }),
                'mobile_no': forms.NumberInput(attrs={
                    'class':"form-control mb-2",
                    'id':"mobile_no",
                    'name':"mobile_no",
                    'placeholder':"mobile no ..."
                }),
                'profile_image': forms.FileInput(attrs={
                    'class':"form-control mb-2",
                    'id':"profile_image",
                    'name':"profile_image",
                    'placeholder':"Profile Image"
                }),
                'date_of_birth': forms.DateInput(attrs={
                    'type': 'date',
                    'class':"form-control mb-2",
                    'id':"date_of_birth",
                    'name':"date_of_birth",
                    'placeholder':"Date of birth"
                }),
            }

