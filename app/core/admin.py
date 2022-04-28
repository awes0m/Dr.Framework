from django.contrib import admin
# We use the Django UserAdmin model as the base
# to create our own custom admin model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models


class UserAdmin(BaseUserAdmin):
    """
    We use the Django UserAdmin model as the base
    to create our own custom admin model

    :param self: UserAdmin (from Django as BaseUserAdmin)
    :return: A custom admin model
    """
    ordering = ['id']
    list_display = ['email', 'name']
    # fieldsets copied from Django UserAdmin
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("name",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    # "groups",
                    # "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": (
            "last_login",
            # "date_joined"
            )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


# Register the user model with the admin site
admin.site.register(models.User, UserAdmin),
