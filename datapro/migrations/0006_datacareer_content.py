# Generated by Django 4.2.19 on 2025-03-07 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datapro', '0005_remove_datacareer_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='datacareer',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
