# Generated by Django 2.2.9 on 2020-01-26 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20200126_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='amount',
            field=models.PositiveIntegerField(null=True),
        ),
    ]