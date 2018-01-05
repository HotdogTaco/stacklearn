# Generated by Django 2.0.1 on 2018-01-05 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180104_1905'),
        ('programming', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivePuzzle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puzzle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programming.GamePuzzle')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Student')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='activepuzzle',
            unique_together={('student', 'puzzle')},
        ),
    ]