# Generated by Django 4.2.6 on 2023-11-01 13:04

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blogpostmodel_pictures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpostmodel',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
