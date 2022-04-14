from django.contrib import admin

# Register your models here.
from gameshop.accounts.models import Profile, GameshopUser


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # inlines = (PetInlineAdmin,)
    list_display = ('first_name', 'last_name',)


@admin.register(GameshopUser)
class ProfileGameshopUser(admin.ModelAdmin):
    list_display = ('username',)
