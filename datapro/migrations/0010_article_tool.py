# Generated by Django 4.2.19 on 2025-03-09 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datapro', '0009_rename_gloosaryterm_glossaryterm'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tool',
            field=models.CharField(default='none', max_length=255),
        ),
    ]
