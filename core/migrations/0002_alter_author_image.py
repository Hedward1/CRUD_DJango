# Generated by Django 3.2 on 2022-07-31 04:45

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='image',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to='core/imgAuthor', variations={}, verbose_name='Image'),
        ),
    ]