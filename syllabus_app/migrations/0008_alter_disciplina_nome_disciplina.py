# Generated by Django 4.2.6 on 2023-10-24 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus_app', '0007_rename_trilhasoptativas_conjuntodisciplinas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='nome_disciplina',
            field=models.CharField(max_length=70),
        ),
    ]
