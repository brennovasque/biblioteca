# Generated by Django 4.1.5 on 2023-01-04 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0002_alter_book_amountpages_alter_book_publicationdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='amountPages',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='publicationDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
