# Generated by Django 2.0.4 on 2018-06-18 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_auto_20180618_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg_info',
            name='usr_id',
            field=models.IntegerField(default=33, primary_key=True, serialize=False, unique=True),
        ),
    ]