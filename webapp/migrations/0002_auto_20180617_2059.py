# Generated by Django 2.0.4 on 2018-06-17 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg_info',
            name='usr_id',
            field=models.IntegerField(default=15, primary_key=True, serialize=False, unique=True),
        ),
    ]