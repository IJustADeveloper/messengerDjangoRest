# Generated by Django 4.2.2 on 2023-07-30 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=models.ImageField(default='avatars/default.jpg', null=True, upload_to='avatars'),
        ),
    ]
