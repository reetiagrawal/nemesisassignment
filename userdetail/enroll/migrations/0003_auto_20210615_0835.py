# Generated by Django 2.2.19 on 2021-06-15 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='username',
        ),
    ]
