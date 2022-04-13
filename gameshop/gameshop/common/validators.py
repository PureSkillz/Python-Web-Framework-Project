from django.core.exceptions import ValidationError


def validate_only_letters(value):
    for el in value:
        if not el.isalpha():
            raise ValidationError("Value must only contain letters")


def positive_price_validator(value):
    if value <= 0:
        raise ValidationError("Price must be more than 0!")


class MaxFileSizeInMbValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.max_size * 1024 * 1024:
            raise ValidationError(f"Max file size is {self.max_size}MB")