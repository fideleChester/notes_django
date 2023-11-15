# Generated by Django 4.2.6 on 2023-11-13 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_rename_matiere_eleve_matieres_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eleve',
            options={'verbose_name_plural': 'Elèves'},
        ),
        migrations.AlterModelOptions(
            name='matiere',
            options={'verbose_name_plural': 'Matières'},
        ),
        migrations.AlterModelOptions(
            name='niveau',
            options={'verbose_name_plural': 'Niveaux'},
        ),
        migrations.RenameField(
            model_name='note',
            old_name='note',
            new_name='eleve',
        ),
        migrations.RemoveField(
            model_name='eleve',
            name='matieres',
        ),
    ]
