from django.urls import path
from .views import (IndexListView,
                    AuthorCreateView,
                    BookCreateView,
                    GenreCreateView,
                    GenreDeleteView,
                    GenreUpdateView,
                    GenreListView)

urlpatterns = [
    path('book/', IndexListView.as_view(), name='IndexListView'),
    path('book/addBook/', BookCreateView.as_view(), name='BookCreateView'),
    path('book/addAuthor/', AuthorCreateView.as_view(), name='AuthorCreateView'),
    path('book/addGenre/', GenreCreateView.as_view(), name='GenreCreateView'),
    path('book/deleteGenre/', GenreDeleteView.as_view(), name='GenreDeleteView'),
    # path('book/updateGenre/', GenreUpdateView.as_view(), name='GenreUpdateView'),
    # path('book/listGenre/', GenreListView.as_view(), name='GenreListView'),
]

