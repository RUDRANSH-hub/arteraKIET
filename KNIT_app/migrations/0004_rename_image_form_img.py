# Generated by Django 3.2 on 2021-07-04 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KNIT_app', '0003_rename_contact_form'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form',
            old_name='Image',
            new_name='img',
        ),
    ]
