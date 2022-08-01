from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Book, Genre
from .forms import BookModelForm, AuthorModelForm


class IndexListView(ListView):
    model = Book
    template_name = "home.html"
    context_object_name = 'books'
    paginate_by = 4


class BookCreateView(CreateView):
    form_class = BookModelForm
    template_name = 'addBook.html'
    success_url = '/core/book/'


class AuthorCreateView(CreateView):
    form_class = AuthorModelForm
    template_name = 'addAuthor.html'
    success_url = '/core/book/'


class GenreCreateView(CreateView):
    model = Genre
    template_name = "addGenre.html"
    success_url = '/core/book/'
    fields = '__all__'


class GenreDeleteView(DeleteView):
    model = Genre
    template_name = "deleteGenre.html"
    success_url = '/core/book/'


class GenreListView(ListView):
    form_class = Genre
    template_name = "listGenre.html"


class GenreUpdateView(UpdateView):
    model = Genre
    fields = ['name', 'email', 'desc', 'img']
    template_name = 'detail.html'
    success_url = ''

