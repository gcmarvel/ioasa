# Generated by Django 2.2.9 on 2019-12-26 14:19

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20191226_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to='../media/article_images'),
        ),
    ]
