# Generated by Django 4.0.2 on 2022-06-11 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snsapp', '0003_identifiedpost_identifiedcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identifiedcomment',
            name='post',
            field=models.ForeignKey(db_column='post_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='snsapp.identifiedpost'),
        ),
    ]
