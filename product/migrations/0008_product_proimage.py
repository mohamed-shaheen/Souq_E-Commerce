# Generated by Django 3.1.5 on 2021-01-17 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20210114_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PROimage',
            field=models.ImageField(blank=True, null=True, upload_to='product/primary/', verbose_name='Image'),
        ),
    ]