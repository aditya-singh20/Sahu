# Generated by Django 2.0.4 on 2018-06-18 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_auto_20180618_0332'),
    ]

    operations = [
        migrations.CreateModel(
            name='resume_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('position', models.TextField()),
                ('univ', models.TextField()),
                ('email', models.TextField(unique=True)),
                ('session', models.TextField()),
                ('ph', models.TextField()),
                ('cph', models.TextField()),
                ('cemail', models.TextField()),
                ('desc', models.TextField()),
                ('cgpa', models.TextField(unique=True)),
                ('skill_1', models.TextField()),
                ('skill_2', models.TextField()),
                ('skill_3', models.TextField()),
                ('skill_4', models.TextField()),
                ('skill_5', models.TextField()),
                ('skill_6', models.TextField()),
                ('xp_1_title', models.TextField()),
                ('xp_2_title', models.TextField()),
                ('xp_3_title', models.TextField()),
                ('xp_4_title', models.TextField()),
                ('xp_5_title', models.TextField()),
                ('xp_6_title', models.TextField()),
                ('xp_1_desc', models.TextField()),
                ('xp_2_desc', models.TextField()),
                ('xp_3_desc', models.TextField()),
                ('xp_4_desc', models.TextField()),
                ('xp_5_desc', models.TextField()),
                ('xp_6_desc', models.TextField()),
                ('xp_1_session', models.DateTimeField()),
                ('xp_2_session', models.DateTimeField()),
                ('xp_3_session', models.DateTimeField()),
                ('xp_4_session', models.DateTimeField()),
                ('xp_5_session', models.DateTimeField()),
                ('xp_6_session', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='reg_info',
            name='usr_id',
            field=models.IntegerField(default=66, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AddField(
            model_name='resume_data',
            name='usr_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.reg_info'),
        ),
    ]
