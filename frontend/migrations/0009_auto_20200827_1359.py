# Generated by Django 3.0.8 on 2020-08-27 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0008_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='Output_image',
            field=models.ImageField(upload_to='media/output'),
        ),
    ]