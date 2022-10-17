# Generated by Django 4.1.2 on 2022-10-17 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_protosheet_ac_protosheet_cha_stat_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request', to='main_app.protocamp')),
                ('character', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='request', to='main_app.protosheet')),
            ],
        ),
        migrations.CreateModel(
            name='Registry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registry', to='main_app.protocamp')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registry', to='main_app.protochar')),
            ],
        ),
    ]