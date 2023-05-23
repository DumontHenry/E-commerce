# Generated by Django 3.2.8 on 2021-11-27 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_rename_state_shippingaddress_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Products/'),
        ),
    ]
