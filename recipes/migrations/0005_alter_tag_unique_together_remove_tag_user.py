# Generated by Django 4.2 on 2023-04-22 22:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_tag_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='tag',
            name='user',
        ),
    ]
