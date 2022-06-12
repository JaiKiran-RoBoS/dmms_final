# Generated by Django 4.0.4 on 2022-05-02 18:31

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0004_remove_complaint_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
        migrations.AlterField(
            model_name='complaint_transformer',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None),
        ),
    ]