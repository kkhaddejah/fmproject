# Generated by Django 4.2.11 on 2024-06-11 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profilepic.jpg', upload_to='pictures/profile_pictures'),
        ),
    ]