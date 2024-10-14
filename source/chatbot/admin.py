from django.contrib import admin
from .models import SystemInstructions

@admin.register(SystemInstructions)
class SystemInstructionsAdmin(admin.ModelAdmin):
    list_display = ('name', 'instructions_preview')
    search_fields = ('name', 'instructions')

    def instructions_preview(self, obj):
        return obj.instructions[:100] + '...' if len(obj.instructions) > 100 else obj.instructions
    instructions_preview.short_description = 'Instructions Preview'