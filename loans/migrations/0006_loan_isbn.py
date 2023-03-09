# Generated by Django 4.1.7 on 2023-03-09 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0005_alter_loan_returned'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='isbn',
            field=models.CharField(default='123456789-1234567', max_length=17, unique=True),
            preserve_default=False,
        ),
    ]
