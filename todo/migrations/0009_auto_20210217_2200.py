# Generated by Django 3.1.6 on 2021-02-17 22:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0008_auto_20210124_1742'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Todo',
            new_name='Task',
        ),
    ]
