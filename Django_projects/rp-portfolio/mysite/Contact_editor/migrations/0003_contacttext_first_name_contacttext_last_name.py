# Generated by Django 4.1.7 on 2023-03-02 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contact_editor', '0002_alter_contacttext_output_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacttext',
            name='first_name',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='contacttext',
            name='last_name',
            field=models.TextField(blank=True),
        ),
    ]
