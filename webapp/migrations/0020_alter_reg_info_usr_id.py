# Generated by Django 3.2.5 on 2021-07-30 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0019_auto_20210730_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg_info',
            name='usr_id',
            field=models.IntegerField(default=96, primary_key=True, serialize=False, unique=True),
        ),
    ]
