# Generated by Django 5.0.6 on 2024-05-24 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0003_contact_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='username',
        ),
    ]