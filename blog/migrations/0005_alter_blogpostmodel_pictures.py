# Generated by Django 4.2.6 on 2023-11-01 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blogpostmodel_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpostmodel',
            name='pictures',
            field=models.ImageField(null=True, upload_to='post_images/'),
        ),
    ]
