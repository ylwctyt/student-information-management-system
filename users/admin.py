from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import MyUser

from .forms import MyUserChangeForm, MyUserCreationForm


# Register your models here.


class MyUserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = MyUserChangeForm
    add_form = MyUserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'email', 'major', 'is_admin', 'is_student', 'is_teacher')
    list_filter = ('is_admin', 'username')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('major',)}),
        ('Permissions', {'fields': ('is_admin', 'is_student', 'is_teacher')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'major', 'password1', 'password2')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(MyUser, MyUserAdmin)
