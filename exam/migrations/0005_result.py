# Generated by Django 2.0.12 on 2020-01-03 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_auto_20191231_1329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=64)),
                ('marks_obtained', models.IntegerField(default=0)),
                ('marks_total', models.IntegerField(default=0)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='exam.Topic')),
            ],
        ),
    ]
