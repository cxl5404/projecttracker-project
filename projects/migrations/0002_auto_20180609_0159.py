# Generated by Django 2.0.2 on 2018-06-09 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='buildingPermitNum',
            new_name='building_Permit_Num',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='customerName',
            new_name='customer_Name',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='pManager',
            new_name='editer',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='electricPermitNum',
            new_name='electric_Permit_Num',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='mechanicalPermitNum',
            new_name='mechanical_Permit_Num',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='phoneNum',
            new_name='phone_Number',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='plumbingPermitNum',
            new_name='plumbing_Permit_Num',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='signPermitNum',
            new_name='sign_Permit_Num',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='zipCode',
            new_name='zip_Code',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='zoningPermitNum',
            new_name='zoning_Permit_Num',
        ),
    ]
