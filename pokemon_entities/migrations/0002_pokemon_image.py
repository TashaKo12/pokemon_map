# Generated by Django 4.1.1 on 2022-09-12 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
