# Generated by Django 4.2.2 on 2023-10-18 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_remove_customer_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='download/uploads/products/'),
        ),
    ]
