# Generated by Django 4.1.5 on 2023-05-28 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0018_book_rent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['firstName']},
        ),
    ]
