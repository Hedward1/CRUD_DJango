# Generated by Django 3.2 on 2022-07-30 20:18

from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Last Update')),
                ('status', models.BooleanField(default=True, verbose_name='Active?')),
                ('author', models.CharField(max_length=100, verbose_name='Author')),
                ('age', models.IntegerField(null=True, verbose_name='Age')),
                ('image', stdimage.models.StdImageField(force_min_size=False, upload_to='authorImage', variations={}, verbose_name='Image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Last Update')),
                ('status', models.BooleanField(default=True, verbose_name='Active?')),
                ('genre', models.CharField(max_length=100, verbose_name='Genre')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='Last Update')),
                ('status', models.BooleanField(default=True, verbose_name='Active?')),
                ('title', models.CharField(max_length=100, verbose_name='Name')),
                ('count', models.IntegerField(default=0, null=True)),
                ('author', models.ManyToManyField(to='core.Author')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.genre')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
