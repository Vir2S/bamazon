from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        ordering = ("id", )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    number_of_pages = models.PositiveSmallIntegerField(default=0)
    authors = models.ManyToManyField(Author, blank=True)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ("id", )

    def __str__(self):
        return self.title
