# Generated by Django 3.0.8 on 2020-08-07 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Djenda_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactos',
            options={'ordering': ['nome']},
        ),
    ]