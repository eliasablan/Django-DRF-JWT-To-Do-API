from django.contrib import admin

from .models import Todo

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
  fieldsets = (
        ('Usuario', {
            'fields': (
                ('user'),
            )
        }),
        ('Todo', {
            'fields': (
                ('todo'),
                ('slug'),
                ('finished','deleted'),
            )
        }),
        ('Metadata', {
            'fields': (
                ('created', 'modified'),
            )
        }),
    )
  prepopulated_fields = {"slug": ("todo",)}
  list_display = ('id', 'user', 'todo', 'finished', 'deleted')
  search_fields = ('todo', 'slug')
  list_filter = ('created', 'modified', 'finished', 'deleted')
  readonly_fields = ('created', 'modified')
