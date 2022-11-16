from .models import Book


def resolve_books(root, info, id):
    return Book.objects.get(pk=id)
