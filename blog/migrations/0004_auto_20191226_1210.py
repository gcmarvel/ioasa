# Generated by Django 3.0 on 2019-12-26 12:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191226_0850'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='big_image',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='article',
            name='medium_image',
        ),
        migrations.RemoveField(
            model_name='article',
            name='small_image',
        ),
        migrations.AddField(
            model_name='article',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 12, 26, 12, 10, 25, 594007)),
        ),
    ]
