# Generated by Django 4.2 on 2023-04-22 21:25

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0003_alter_recipe_user_tag_recipe_tags'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together={('name', 'user')},
        ),
    ]
