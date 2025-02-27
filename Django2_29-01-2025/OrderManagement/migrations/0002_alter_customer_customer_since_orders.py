# Generated by Django 5.1.4 on 2025-01-28 15:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD_APP', '0002_product_qty'),
        ('OrderManagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_since',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=20, null=True)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.FloatField(default=0)),
                ('amount', models.FloatField(default=0)),
                ('gst_amount', models.FloatField(default=0)),
                ('bill_amount', models.FloatField(default=0)),
                ('customer_reference', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='OrderManagement.customer')),
                ('product_reference', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CRUD_APP.product')),
            ],
        ),
    ]
