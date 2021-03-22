from django.contrib import admin

# Register your models here.
from .models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'lastname',
        'nationality',
    )

    search_fields = (
        'name',
        'nationality',
    )
    list_filter = (
        'nationality',
    )

class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'resume',
        'author',
    )

    search_fields = (
        'title',
        'author',
    )
    list_filter = (
        'author',
    )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)