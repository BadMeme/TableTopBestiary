# Generated by Django 4.1.2 on 2022-10-17 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_regrequest_character'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protosheet',
            name='race',
            field=models.CharField(choices=[('Human', 'Human'), ('Elf', 'Elf'), ('Dwarf', 'Dwarf'), ('Halfling', 'Halfling'), ('Half-Elf', 'Half-Elf'), ('Half-Orc', 'Half-Orc'), ('Gnome', 'Gnome'), ('Dragonborn', 'Dragonborn'), ('Tiefling', 'Tiefling')], default='Human', max_length=10),
        ),
    ]
