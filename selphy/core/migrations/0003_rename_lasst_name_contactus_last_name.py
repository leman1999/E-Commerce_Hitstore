# Generated by Django 4.0.10 on 2023-10-13 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_contactus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='lasst_name',
            new_name='last_name',
        ),
    ]