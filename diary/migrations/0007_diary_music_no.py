# Generated by Django 3.2.13 on 2022-04-28 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0006_auto_20220428_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='music_no',
            field=models.IntegerField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]