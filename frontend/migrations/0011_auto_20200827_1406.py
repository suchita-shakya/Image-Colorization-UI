# Generated by Django 3.0.8 on 2020-08-27 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0010_auto_20200827_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='Input_image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='Output_image',
            field=models.ImageField(upload_to=''),
        ),
    ]