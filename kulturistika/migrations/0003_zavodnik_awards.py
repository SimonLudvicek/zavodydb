# Generated by Django 4.2.2 on 2023-06-14 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kulturistika', '0002_zavodnik_trener'),
    ]

    operations = [
        migrations.AddField(
            model_name='zavodnik',
            name='awards',
            field=models.ManyToManyField(to='kulturistika.oceneni'),
        ),
    ]
