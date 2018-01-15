from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import MyUser, Student

from .forms import MyUserChangeForm, MyUserCreationForm, StudentCreationForm


# Register your models here.

# TODO:set the default 'is_active' and 'is_staff' = true

class MyUserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = MyUserChangeForm
    add_form = MyUserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'email', 'major', 'is_staff', 'is_active', 'is_admin', 'is_student', 'is_teacher')
    list_filter = ('is_admin', 'is_student', 'is_teacher', 'username')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('major',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_admin', 'is_student', 'is_teacher')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'major', 'password1', 'password2', 'is_admin', 'is_student', 'is_teacher')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(MyUser, MyUserAdmin)
