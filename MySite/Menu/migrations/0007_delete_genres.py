# Generated by Django 4.1.5 on 2023-01-04 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0006_remove_book_genres'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Genres',
        ),
    ]