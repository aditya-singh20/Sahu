# Generated by Django 2.0.4 on 2018-06-17 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20180618_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg_info',
            name='usr_id',
            field=models.IntegerField(default=135, primary_key=True, serialize=False, unique=True),
        ),
    ]
