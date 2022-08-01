from .models import Author, Book, Genre
from django.forms import ModelForm


class AuthorModelForm(ModelForm):
    class Meta:
        model = Author
        fields = ['author', 'age', 'image']


class GenreModelForm(ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'


class BookModelForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'genre', 'count', 'author']
