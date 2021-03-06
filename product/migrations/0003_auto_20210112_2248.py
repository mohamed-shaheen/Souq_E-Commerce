# Generated by Django 3.1.5 on 2021-01-12 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20210110_0011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='PROCost',
            new_name='PROcost',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='PROCreated',
            new_name='PROcreated',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='PRODesc',
            new_name='PROdesc',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='PROName',
            new_name='PROname',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='PROPrice',
            new_name='PROprice',
        ),
        migrations.RenameField(
            model_name='productimage',
            old_name='PRDIImage',
            new_name='PRDIimage',
        ),
        migrations.RenameField(
            model_name='productimage',
            old_name='PRDIProduct',
            new_name='PRDIproduct',
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CATname', models.CharField(max_length=50)),
                ('CATdesc', models.TextField()),
                ('CATimg', models.ImageField(upload_to='category/')),
                ('CATparent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
        ),
    ]
