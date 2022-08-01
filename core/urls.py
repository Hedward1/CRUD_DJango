from django.urls import path
from views.book_view import (IndexListView,
                             BookCreateView)

from views.genre_views import (GenreListView,
                               GenreDeleteView,
                               GenreUpdateView,
                               GenreCreateView)

from views.author_view import (AuthorCreateView)


urlpatterns = [
    path('', IndexListView.as_view(), name='IndexListView'),
    path('addBook/', BookCreateView.as_view(), name='BookCreateView'),
    path('addAuthor/', AuthorCreateView.as_view(), name='AuthorCreateView'),
    path('listGenre/', GenreListView.as_view(), name='GenreListView'),
    path('addGenre/', GenreCreateView.as_view(), name='GenreCreateView'),
    path('<int:pk>/updateGenre/', GenreUpdateView.as_view(), name='GenreUpdateView'),
    path('<int:pk>/deleteGenre/', GenreDeleteView.as_view(), name='GenreDeleteView'),
]
