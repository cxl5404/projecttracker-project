# Generated by Django 2.0.2 on 2018-06-10 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_remove_project_editer'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='BP_Status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='EP_Status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='MP_Status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='PP_Status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='SP_Status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='ZP_Status',
            field=models.IntegerField(default=0),
        ),
    ]
