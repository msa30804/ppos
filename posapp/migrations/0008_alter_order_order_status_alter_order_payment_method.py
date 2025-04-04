# Generated by Django 5.0.2 on 2025-04-03 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posapp', '0007_alter_product_options_remove_product_barcode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('Cash', 'Cash'), ('Card', 'Card'), ('Mobile', 'Mobile Payment')], default='Cash', max_length=50),
        ),
    ]
