from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Book, Genre
from .forms import BookModelForm, AuthorModelForm, GenreModelForm


class IndexListView(ListView):
    model = Book
    template_name = "home.html"
    queryset = Book.objects.all()
    # context_object_name = 'book'
    paginate_by = 4


class BookCreateView(CreateView):
    form_class = BookModelForm
    template_name = 'addBook.html'
    success_url = '/core/'


class AuthorCreateView(CreateView):
    form_class = AuthorModelForm
    template_name = 'addAuthor.html'
    success_url = '/core/'


class GenreListView(ListView):
    form_class = Genre
    template_name = "listGenre.html"
    queryset = Genre.objects.all()
    context_object_name = 'genres'


class GenreCreateView(CreateView):
    model = Genre
    template_name = "addGenre.html"
    success_url = reverse_lazy('GenreListView')
    fields = '__all__'


class GenreUpdateView(UpdateView):
    model = Genre
    template_name = 'addGenre.html'
    fields = ['genreName']
    success_url = reverse_lazy('GenreListView')


class GenreDeleteView(DeleteView):
    model = Genre
    template_name = "deleteGenre.html"
    success_url = reverse_lazy('GenreListView')
