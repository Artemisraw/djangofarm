# Generated by Django 3.2.8 on 2024-02-22 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0005_feedback_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orders',
            options={'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
    ]
