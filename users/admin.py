from users.models import CustomUser
from django.contrib import admin


@admin.register(CustomUser)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ['last_name', 'password']
