from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from ..models import Genre


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
