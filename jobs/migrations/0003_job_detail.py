# Generated by Django 5.0.2 on 2024-02-21 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_alter_job_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='detail',
            field=models.TextField(default='Title'),
            preserve_default=False,
        ),
    ]
