from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from ..forms import AuthorModelForm
from ..models import Author


class AuthorCreateView(CreateView):
    form_class = AuthorModelForm
    template_name = 'addAuthor.html'
    success_url = '/core/'


class AuthorListView(ListView):
    form_class = Author
    template_name = "listGenre.html"
    queryset = Author.objects.all()
    context_object_name = 'genres'


class AuthorCreateView(CreateView):
    model = Author
    template_name = "addGenre.html"
    success_url = reverse_lazy('GenreListView')
    fields = '__all__'


class AuthorUpdateView(UpdateView):
    model = Author
    template_name = 'addGenre.html'
    fields = ['genreName']
    success_url = reverse_lazy('GenreListView')


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = "deleteGenre.html"
    success_url = reverse_lazy('GenreListView')
