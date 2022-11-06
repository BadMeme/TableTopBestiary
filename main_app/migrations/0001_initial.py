# Generated by Django 4.1.2 on 2022-10-17 01:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProtoChar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField(max_length=500)),
                ('img', models.CharField(default='https://mythologian.net/wp-content/uploads/2018/02/Metatrons-Cube-Symbol-Flower-Of-Life-Meaning-Symbolism-Story-1024x1024.jpg', max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='protochar', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='ProtoSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race', models.CharField(choices=[('Human', 'Human'), ('Elf', 'Elf'), ('Dwarf', 'Dwarf'), ('Halfling', 'Halfling'), ('Half-Elf', 'Half-Elf'), ('Half-Orc', 'Half-Orc'), ('Gnome', 'Gnome'), ('Drg', 'Dragonborn'), ('Tie', 'Tiefling')], default='Human', max_length=10)),
                ('base_class', models.CharField(choices=[('Human', 'Human'), ('Elf', 'Elf'), ('Dwarf', 'Dwarf'), ('Halfling', 'Halfling'), ('Half-Elf', 'Half-Elf'), ('Half-Orc', 'Half-Orc'), ('Gnome', 'Gnome'), ('Drg', 'Dragonborn'), ('Tie', 'Tiefling')], default='Artificer', max_length=10)),
                ('str_save', models.BooleanField(default=False)),
                ('dex_save', models.BooleanField(default=False)),
                ('con_save', models.BooleanField(default=False)),
                ('int_save', models.BooleanField(default=False)),
                ('wis_save', models.BooleanField(default=False)),
                ('cha_save', models.BooleanField(default=False)),
                ('acrobatics', models.BooleanField(default=False)),
                ('animal_handling', models.BooleanField(default=False)),
                ('arcana', models.BooleanField(default=False)),
                ('athletics', models.BooleanField(default=False)),
                ('deception', models.BooleanField(default=False)),
                ('history', models.BooleanField(default=False)),
                ('insight', models.BooleanField(default=False)),
                ('intimidation', models.BooleanField(default=False)),
                ('investigation', models.BooleanField(default=False)),
                ('medicine', models.BooleanField(default=False)),
                ('nature', models.BooleanField(default=False)),
                ('perception', models.BooleanField(default=False)),
                ('performance', models.BooleanField(default=False)),
                ('persuasion', models.BooleanField(default=False)),
                ('religion', models.BooleanField(default=False)),
                ('sleight_of_hand', models.BooleanField(default=False)),
                ('survival', models.BooleanField(default=False)),
                ('protochar', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.protochar')),
            ],
        ),
        migrations.CreateModel(
            name='ProtoCamp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('info', models.CharField(max_length=500)),
                ('img', models.CharField(default='https://cdn4.iconfinder.com/data/icons/video-game-items-concepts/128/magic-spell-book-open-512.png', max_length=500)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]