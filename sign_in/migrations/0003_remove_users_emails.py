# Generated by Django 2.0.5 on 2018-05-16 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sign_in', '0002_auto_20180514_1401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='emails',
        ),
    ]
