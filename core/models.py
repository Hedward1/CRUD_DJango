from django.db import models
from stdimage import StdImageField


class Base(models.Model):
    created = models.DateTimeField('Creation', auto_now_add=True)
    last_update = models.DateTimeField('Last Update', auto_now=True)
    status = models.BooleanField('Active?', default=True)

    class Meta:
        abstract = True


class Author(Base):
    author = models.CharField('Author', max_length=100)
    age = models.IntegerField('Age', null=True, blank=True)
    image = StdImageField('Image', upload_to='core/imgAuthor', delete_orphans=True, null=True, blank=True)

    def __str__(self):
        return self.author


class Genre(Base):
    genre = models.CharField('Genre', max_length=100)

    def __str__(self):
        return self.genre


class Book (Base):
    title = models.CharField('Name', max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    count = models.IntegerField(null=True, default=0)
    author = models.ManyToManyField(Author)

    def __str__(self):
        return self.title
