# Generated by Django 4.2.3 on 2023-09-08 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_item_label_alter_item_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='discount_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(),
        ),
    ]