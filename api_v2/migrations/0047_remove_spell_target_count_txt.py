# Generated by Django 3.2.20 on 2024-02-29 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_v2', '0046_spell_target_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spell',
            name='target_count_txt',
        ),
    ]
