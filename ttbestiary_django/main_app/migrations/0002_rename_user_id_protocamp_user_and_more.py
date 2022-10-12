# Generated by Django 4.1.2 on 2022-10-11 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='protocamp',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='protochar',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AddField(
            model_name='protosheet',
            name='char',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.protochar'),
        ),
    ]
