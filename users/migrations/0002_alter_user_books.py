# Generated by Django 4.1.7 on 2023-03-08 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='books',
            field=models.ManyToManyField(blank=True, related_name='follow', to='books.book'),
        ),
    ]
