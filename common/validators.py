from django.core.exceptions import ValidationError


def file_validator(value):
    if not value.endwith('png'):
        raise ValidationError

