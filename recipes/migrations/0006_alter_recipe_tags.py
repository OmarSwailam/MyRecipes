# Generated by Django 4.2 on 2023-04-22 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_alter_tag_unique_together_remove_tag_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(related_name='tags', to='recipes.tag'),
        ),
    ]
