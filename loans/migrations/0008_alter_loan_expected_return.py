# Generated by Django 4.1.7 on 2023-03-10 11:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("loans", "0007_alter_loan_isbn"),
    ]

    operations = [
        migrations.AlterField(
            model_name="loan",
            name="expected_return",
            field=models.DateTimeField(),
        ),
    ]
