# Generated by Django 4.1.7 on 2023-03-23 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Contact_editor', '0007_contacttext_academic_title_contacttext_adress_detail_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacttext',
            old_name='firstName',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='contacttext',
            old_name='lastName',
            new_name='last_name',
        ),
    ]
