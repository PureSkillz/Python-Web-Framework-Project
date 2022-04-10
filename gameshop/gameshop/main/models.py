from django.contrib.auth import get_user_model
from django.db import models

from gameshop.common.validators import positive_price_validator, MaxFileSizeInMbValidator

UserModel = get_user_model()


class Item(models.Model):
    MAX_NAME_LENGTH = 30
    MAX_DESCRIPTION_LENGTH = 200

    name = models.CharField(
        max_length=MAX_NAME_LENGTH
    )

    price = models.FloatField(
        validators=(positive_price_validator,)
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    description = models.TextField(
        null=True,
        blank=True,
        max_length=MAX_DESCRIPTION_LENGTH
    )

    # image = models.ImageField(
    #     validators=(MaxFileSizeInMbValidator(10),)
    # )

    def get_class_name(self):
        return self.__class__.__name__

    def __str__(self):
        return f"{self.name}"

    class Meta:
        abstract = True


class Game(Item):
    PC = "PC"
    CONSOLE = "Console"

    PLATFORMS = [(x, x) for x in (PC, CONSOLE)]

    MAX_DEV_NAME_LENGTH = 20

    platform = models.CharField(
        max_length=max(len(x) for (x,_) in PLATFORMS),
        choices=PLATFORMS,
    )

    developer = models.CharField(
        null=True,
        blank=True,
        max_length=MAX_DEV_NAME_LENGTH,
    )


class Periphery(Item):
    NEW = "New"
    USED = "Used"

    STATUSES = [(x, x) for x in (NEW, USED)]

    warranty = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
    )

    condition = models.CharField(
        max_length=max(len(x) for (x, _) in STATUSES),
        choices=STATUSES,
    )



