# Generated by Django 2.2.7 on 2019-12-05 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enfants', '0003_auto_20191205_1228'),
        ('professionnels', '0001_initial'),
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('session_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('enfant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='enfants.HandicapEnfant')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('habitude', models.CharField(choices=[('O', 'Oui'), ('N', 'Non'), ('V', 'Voudrais')], max_length=9, null=True)),
                ('aime', models.CharField(choices=[('O', 'Oui'), ('N', 'Non')], max_length=3, null=True)),
                ('aide', models.CharField(choices=[('O', 'Oui'), ('N', 'Non')], max_length=3, null=True)),
                ('content', models.CharField(choices=[('O', 'Oui'), ('N', 'Non')], max_length=3, null=True)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='image', to='images.Image')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='session_question.Session')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('note_id', models.AutoField(primary_key=True, serialize=False)),
                ('note_aime', models.CharField(max_length=255, null=True)),
                ('note_aide', models.CharField(max_length=255, null=True)),
                ('note_statisfaction', models.CharField(max_length=255, null=True)),
                ('professionnel_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='professionnel', to='professionnels.Professionnel')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='session_question.Question')),
            ],
        ),
    ]
