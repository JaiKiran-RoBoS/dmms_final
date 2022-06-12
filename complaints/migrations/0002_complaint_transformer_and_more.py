# Generated by Django 4.0.4 on 2022-04-27 05:54

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint_Transformer',
            fields=[
                ('complaint_id', models.AutoField(primary_key=True, serialize=False)),
                ('complaint_trans', models.CharField(choices=[('Transformer 1', 'Transformer 1'), ('Transformer 2', 'Transformer 2'), ('Transformer 3', 'Transformer 3'), ('Transformer 4', 'Transformer 4'), ('Transformer 5', 'Transformer 5'), ('Transformer 6', 'Transformer 6'), ('Transformer 7', 'Transformer 7')], default='Transformer 1', max_length=20, null=True)),
                ('complaint_nature', models.CharField(choices=[('Damaged Transformer AB', 'Damaged Transformer AB'), ('Damaged LAs', 'Damaged LAs'), ('Damaged DO Set', 'Damaged DO Set'), ('Damaged HT drops', 'Damaged HT drops'), ('HT Bush Damaged', 'HT Bush Damaged'), ('LT Bush Damaged', 'LT Bush Damaged'), ('Oil Leakage', 'Oil Leakage'), ('Burned LT cables', 'Burned LT cables'), ('Damaged Fuse units', 'Damaged Fuse units'), ('Yard cleaning Required', 'Yard cleaning Required'), ('Earthing required', 'Earthing required'), ('Load unbalance', 'Load unbalance'), ('Body painting', 'Body painting'), ('Low Oil Level', 'Low Oil Level'), ('Damaged Breather', 'Damaged Breather')], default='Damaged Transformer AB', max_length=40, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='complaint',
            name='complaint_category',
            field=models.CharField(choices=[('HT', 'HT'), ('LT', 'LT')], default='HT', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='complaint_nature',
            field=models.CharField(choices=[('Touching', 'Touching'), ('Creepings', 'Creepings'), ('Low Hanging Conductor', 'Low Hanging Conductor'), ('Damaged Insulator', 'Damaged Insulator'), ('Slanted Pole', 'Slanted Pole'), ('Damaged Pole', 'Damaged Pole'), ('Damaged Line AB Switch', 'Damaged Line AB Switch'), ('Clearance Issue', 'Clearance Issue'), ('Broken Stay', 'Broken Stay'), ('Damaged Strut', 'Damaged Strut')], default='Touching', max_length=40, null=True),
        ),
    ]