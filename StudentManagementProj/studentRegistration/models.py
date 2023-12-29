from django.db import models
from django.core.validators import EmailValidator

from .validations import validate_mobile_no, validate_age

class StudentRegistration(models.Model):
    st_name = models.CharField(max_length=255)
    email = models.EmailField(validators=[EmailValidator]) # type: ignore
    mobile_no = models.IntegerField(validators=[validate_mobile_no])
    profile_image = models.ImageField(upload_to='student/pic/')
    date_of_birth = models.DateField(validators=[validate_age])
    add_date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.st_name