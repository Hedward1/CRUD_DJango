# Generated by Django 3.2 on 2022-08-01 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_author_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='genre',
            old_name='genre',
            new_name='genreName',
        ),
    ]
