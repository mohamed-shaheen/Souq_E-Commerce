# Generated by Django 3.1.5 on 2021-01-27 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_product_pro'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='PRO',
            new_name='PROslug',
        ),
    ]
