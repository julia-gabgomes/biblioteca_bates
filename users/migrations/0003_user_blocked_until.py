# Generated by Django 4.1.7 on 2023-03-14 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='blocked_until',
            field=models.DateField(null=True),
        ),
    ]
