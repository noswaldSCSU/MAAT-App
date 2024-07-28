# Generated by Django 5.0.7 on 2024-07-28 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maat_app', '0002_remove_trial_movement_alter_participant_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='background_color',
            field=models.CharField(default='#ffffff', max_length=7),
        ),
        migrations.AddField(
            model_name='experiment',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='backgrounds/'),
        ),
        migrations.AddField(
            model_name='trial',
            name='background_color',
            field=models.CharField(default='#ffffff', max_length=7),
        ),
        migrations.AddField(
            model_name='trial',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='backgrounds/'),
        ),
    ]