from django.core.exceptions import ValidationError
from datetime import date
 
def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - \
         ((today.month, today.day) <
         (birthDate.month, birthDate.day))
 
    return age

def validate_age(dob):
    age = calculateAge(dob)
    if age < 18:
        raise ValidationError("The student age should be 18.")


def validate_mobile_no(m_no):
    if find_m_no_length(m_no) != 10:
        raise ValidationError("Mobile Number need to be 10 digits.")

def find_m_no_length(m_no):
    count = 0
    while m_no > 0:
        m_no = m_no // 10
        count += 1
    return count 