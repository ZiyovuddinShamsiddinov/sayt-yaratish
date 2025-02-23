# Generated by Django 5.1.6 on 2025-02-20 17:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('birth_date', models.DateField(blank=True)),
                ('created_ed', models.DateTimeField(auto_now_add=True)),
                ('update_ed', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='aftosalon',
            options={'ordering': ['-created'], 'verbose_name': 'Aftosolon', 'verbose_name_plural': 'Aftosolons'},
        ),
        migrations.AddField(
            model_name='aftosalon',
            name='aftosalon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='configapp.categories'),
        ),
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='configapp.car_model'),
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]
