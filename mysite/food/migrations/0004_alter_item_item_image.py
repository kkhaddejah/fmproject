# Generated by Django 4.2.11 on 2024-06-02 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://www.food4fuel.com/wp-content/uploads/woocommerce-placeholder-600x600.png', max_length=2000),
        ),
    ]
