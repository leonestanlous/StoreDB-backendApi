# Generated by Django 3.2.12 on 2022-02-20 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20220216_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale_products',
            name='price',
            field=models.FloatField(),
        ),
    ]
