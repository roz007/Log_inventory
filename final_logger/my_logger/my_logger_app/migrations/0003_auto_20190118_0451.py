# Generated by Django 2.1.5 on 2019-01-18 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_logger_app', '0002_variant_variant_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='Brand',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='items',
            old_name='Category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='items',
            old_name='Product_code',
            new_name='product_code',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='Attribute_name',
            new_name='attribute_name',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='Attribute_value',
            new_name='attribute_value',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='name',
            new_name='item',
        ),
        migrations.RenameField(
            model_name='variant',
            old_name='name',
            new_name='item',
        ),
        migrations.RemoveField(
            model_name='variant',
            name='property_name',
        ),
        migrations.AddField(
            model_name='property',
            name='variant',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='my_logger_app.Variant'),
            preserve_default=False,
        ),
    ]