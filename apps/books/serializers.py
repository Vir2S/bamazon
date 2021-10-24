from rest_framework import serializers

from apps.books.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            "id",
            "first_name",
            "last_name",
        )


class BookSerializer(serializers.ModelSerializer):
    authors_details = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = (
            "id",
            "title",
            "description",
            "number_of_pages",
            "authors",
            "authors_details",
        )

    @staticmethod
    def get_authors_details(obj: Book):
        return AuthorSerializer(obj.authors.all(), many=True).data
