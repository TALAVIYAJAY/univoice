# Generated by Django 5.1.6 on 2025-02-28 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medic', '0002_alter_tln_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tln',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
