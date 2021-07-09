from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Profile
from income.models import Income


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_per_page = 7
    list_display = (
        "id",
        "user",
        "upper_case_name",
    )
    list_display_links = ("id", "user")
    search_fields = (
        "user__email",
        "user__username",
        "user__first_name",
        "user__last_name",
    )
    list_filter = (
        "user__is_active",
        "user__is_staff",
    )
    """
    A string representing a property in modeladmin. The behavior is the same as the callable object.But self at this time is the model instance. Like this:
    """

    @admin.display(description="Name")
    def upper_case_name(self, obj):
        return ("%s" % (obj.user.username)).upper()


# For both admins to see each other in one, it is done in the following way.
class ProfileInline(admin.StackedInline):
    """Profile in-line admin for users."""

    model = Profile
    can_delete = False
    verbose_name_plural = "Profile"


class IncomeInline(admin.StackedInline):
    """Income in-line admin for users."""

    model = Income
    can_delete = False
    can_update = False
    verbose_name_plural = "Income"


class UserAdmin(BaseUserAdmin):
    """Add income,profile admin to base user admin."""

    inlines = [
        ProfileInline,
        IncomeInline,
    ]

    list_display = (
        "username",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
# Changing admin header
admin.site.site_header = "Income Expense Manager"
