# Generated by Django 4.1.2 on 2022-10-17 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_alter_registry_member_alter_regrequest_campaign'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Registry',
            new_name='MemberList',
        ),
        migrations.RenameModel(
            old_name='RegRequest',
            new_name='MemberRequest',
        ),
    ]
