from django.contrib import admin
from tuites.models import Tuite

# Register your models here.
class TuiteAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'date_created')
    

admin.site.register(Tuite, TuiteAdmin)
