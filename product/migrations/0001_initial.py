# Generated by Django 3.1.5 on 2021-01-09 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PROName', models.CharField(max_length=100)),
                ('PRODesc', models.TextField()),
                ('PROPrice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('PROCost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('PROCreated', models.DateTimeField()),
            ],
        ),
    ]
