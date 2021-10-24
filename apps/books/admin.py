from django.contrib import admin

from . models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
    )


class BookAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "number_of_pages",
    )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
