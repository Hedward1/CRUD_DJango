from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Book
from .forms import BookModelForm, AuthorModelForm


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
