# Generated by Django 2.0.12 on 2021-01-27 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20210127_0803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livetradingdata',
            name='close_value',
        ),
        migrations.AddField(
            model_name='livetradingdata',
            name='company_name_symbol',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='livetradingdata',
            name='qty',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='livetradingdata',
            name='change_percent_value',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='livetradingdata',
            name='date_value',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='livetradingdata',
            name='high_value',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='livetradingdata',
            name='low_value',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='livetradingdata',
            name='open_value',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
