# Generated by Django 4.1.7 on 2023-02-22 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contact_editor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacttext',
            name='output_text',
            field=models.TextField(blank=True),
        ),
    ]
