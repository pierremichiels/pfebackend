# Generated by Django 3.0 on 2019-12-05 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('session_question', '0002_auto_20191205_1445'),
        ('professionnels', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Professionnel',
        ),
    ]
