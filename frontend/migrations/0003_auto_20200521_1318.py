# Generated by Django 3.0.6 on 2020-05-21 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_auto_20200521_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='Image_name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='image',
            name='Input_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='image',
            name='Output_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
