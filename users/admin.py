from django.contrib import admin

from tuites.models import Tuite
from users.models import User

# Register your models here.


class InlineTuiteAdmin(admin.StackedInline):
    model = Tuite


class UserAdmin(admin.ModelAdmin):
    filter_horizontal = ('following', )
    fieldsets = (
        ('Dados pessoais', {
            'fields': ('username', 'email', 'date_joined'),
        }),
        ('Tuirer', {
            'fields': ('following', )
        })
    )

admin.site.register(User, UserAdmin)
