# Generated by Django 4.1.2 on 2022-10-17 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_protocamp_user_alter_protosheet_base_class'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protosheet',
            name='protochar',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='protosheet', to='main_app.protochar'),
        ),
    ]
