# Generated by Django 4.2.6 on 2023-11-25 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blogpostmodel_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpostmodel',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]