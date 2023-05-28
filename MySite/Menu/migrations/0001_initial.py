# Generated by Django 4.1.5 on 2023-01-04 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=15)),
                ('lastName', models.CharField(max_length=20)),
                ('birthDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('amountPages', models.PositiveIntegerField()),
                ('publicationDate', models.DateField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Menu.author')),
            ],
        ),
    ]
