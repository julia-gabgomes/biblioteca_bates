# Generated by Django 4.1.7 on 2023-03-08 12:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("copies", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="copy",
            name="is_loaned",
            field=models.BooleanField(default=False),
        ),
    ]
