from django.contrib import admin
from list_app.models import List


admin.site.register(List)


class ListAdmin(admin.ModelAdmin):

    list_display = ['id', 'list', 'status', 'created_at']
    list_filter = ['list']
    search_fields = ['list', 'status']
    fields = ['list', 'status', 'created_at']
    readonly_fields = ['created_at']