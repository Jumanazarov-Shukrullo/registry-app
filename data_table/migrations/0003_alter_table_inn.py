# Generated by Django 5.0.4 on 2024-04-29 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_table', '0002_alter_table_abbreviated_name_alter_table_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='inn',
            field=models.BigIntegerField(),
        ),
    ]
