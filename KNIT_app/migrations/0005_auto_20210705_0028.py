# Generated by Django 3.2 on 2021-07-04 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KNIT_app', '0004_rename_image_form_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='catagory',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='form',
            name='desc',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='form',
            name='img',
            field=models.ImageField(default='', upload_to='KNIT_App/image'),
        ),
    ]
