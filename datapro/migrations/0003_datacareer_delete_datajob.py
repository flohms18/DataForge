# Generated by Django 4.2.19 on 2025-03-07 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datapro', '0002_datajob_delete_dataprofession'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataCareer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='DataJob',
        ),
    ]
