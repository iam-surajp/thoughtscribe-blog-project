# Generated by Django 4.2.6 on 2023-12-06 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_blogpostmodel_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpostmodel',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
