# Generated by Django 2.2.19 on 2021-06-15 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0003_auto_20210615_0835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
    ]
