# Generated by Django 4.1.7 on 2023-03-08 12:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("copies", "0002_copy_is_loaned"),
    ]

    operations = [
        migrations.RenameField(
            model_name="copy",
            old_name="is_loanable",
            new_name="is_prime",
        ),
    ]
