# Generated by Django 3.2.20 on 2023-10-03 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v2', '0014_alter_featbenefit_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='backgroundbenefit',
            name='type',
            field=models.CharField(blank=True, choices=[('ability_score_increase', 'Ability Score Increase'), ('skill_proficiency', 'Skill Proficiency'), ('tool_proficiency', 'Tool Proficiency'), ('language', 'Language'), ('equipment', 'Equipment'), ('feature', 'Feature'), ('connection', 'Connection'), ('memento', 'Memento')], help_text='Benefit type.', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='featbenefit',
            name='type',
            field=models.CharField(blank=True, choices=[('ability_score_increase', 'Ability Score Increase'), ('skill_proficiency', 'Skill Proficiency'), ('tool_proficiency', 'Tool Proficiency'), ('language', 'Language'), ('equipment', 'Equipment'), ('feature', 'Feature'), ('connection', 'Connection'), ('memento', 'Memento')], help_text='Benefit type.', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='trait',
            name='type',
            field=models.CharField(blank=True, choices=[('ability_score_increase', 'Ability Score Increase'), ('skill_proficiency', 'Skill Proficiency'), ('tool_proficiency', 'Tool Proficiency'), ('language', 'Language'), ('equipment', 'Equipment'), ('feature', 'Feature'), ('connection', 'Connection'), ('memento', 'Memento')], help_text='Benefit type.', max_length=200, null=True),
        ),
    ]
