# Generated by Django 4.2.11 on 2024-06-11 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='.jpg', upload_to='profile_pictures'),
        ),
    ]