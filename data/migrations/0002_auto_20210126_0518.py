# Generated by Django 3.0.6 on 2021-01-26 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
    ]
