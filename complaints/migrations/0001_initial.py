# Generated by Django 4.0.4 on 2022-04-27 04:46

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('complaint_id', models.AutoField(primary_key=True, serialize=False)),
                ('complaint_category', models.CharField(choices=[('ht', 'HT'), ('lt', 'LT')], default='HT', max_length=20, null=True)),
                ('complaint_nature', models.CharField(choices=[('ht', 'HT'), ('lt', 'LT')], default='HT', max_length=20, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]