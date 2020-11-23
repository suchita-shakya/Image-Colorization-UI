# Generated by Django 3.0.8 on 2020-08-27 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0007_auto_20200711_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('roll_no', models.CharField(max_length=10)),
                ('image', models.ImageField(upload_to='assets/images')),
            ],
        ),
    ]