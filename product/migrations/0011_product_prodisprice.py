# Generated by Django 3.1.5 on 2021-01-27 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20210127_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PROdisprice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='Discount Price'),
            preserve_default=False,
        ),
    ]
