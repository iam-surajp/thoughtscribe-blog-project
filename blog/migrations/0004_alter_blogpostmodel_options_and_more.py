# Generated by Django 4.2.6 on 2023-11-01 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpostmodel',
            options={'ordering': ('-date',)},
        ),
        migrations.RemoveField(
            model_name='blogpostmodel',
            name='urls',
        ),
        migrations.RemoveField(
            model_name='categorymodel',
            name='url',
        ),
    ]
