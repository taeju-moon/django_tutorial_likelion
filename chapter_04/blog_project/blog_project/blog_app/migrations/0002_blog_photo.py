# Generated by Django 3.2.4 on 2022-02-22 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='photo',
            field=models.ImageField(blank=True, upload_to='blog_photo'),
        ),
    ]
