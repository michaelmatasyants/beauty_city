# Generated by Django 5.0.1 on 2024-01-26 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='surname',
            new_name='lastname',
        ),
    ]
