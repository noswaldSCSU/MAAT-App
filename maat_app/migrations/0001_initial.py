# Generated by Django 5.0.7 on 2024-07-27 15:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experiment_id', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('instructions', models.TextField(blank=True, null=True)),
                ('num_trials', models.IntegerField(default=0)),
                ('text_size', models.IntegerField(default=100)),
                ('text_increase_size', models.IntegerField(default=120)),
                ('text_decrease_size', models.IntegerField(default=80)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_id', models.CharField(max_length=100, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('experiment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maat_app.experiment')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maat_app.participant')),
            ],
        ),
        migrations.AddField(
            model_name='participant',
            name='experiments',
            field=models.ManyToManyField(through='maat_app.Participation', to='maat_app.experiment'),
        ),
        migrations.CreateModel(
            name='Trial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_order', models.IntegerField()),
                ('block_name', models.CharField(max_length=50)),
                ('stimuli', models.CharField(max_length=255)),
                ('valence', models.IntegerField()),
                ('random_fixation', models.IntegerField()),
                ('movement', models.IntegerField()),
                ('experiment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trials', to='maat_app.experiment')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_time', models.FloatField()),
                ('accuracy', models.IntegerField()),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maat_app.participant')),
                ('trial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maat_app.trial')),
            ],
        ),
    ]
