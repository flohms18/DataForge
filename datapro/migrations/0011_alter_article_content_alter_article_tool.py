# Generated by Django 4.2.19 on 2025-03-09 17:37

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datapro', '0010_article_tool'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='tool',
            field=models.CharField(default='one', max_length=255),
        ),
    ]
