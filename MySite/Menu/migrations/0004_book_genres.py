# Generated by Django 4.1.5 on 2023-01-04 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0003_alter_book_amountpages_alter_book_publicationdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='genres',
            field=models.CharField(blank=True, choices=[('Terror', 'Terror'), ('Suspense', 'Suspense')], max_length=25),
        ),
    ]
