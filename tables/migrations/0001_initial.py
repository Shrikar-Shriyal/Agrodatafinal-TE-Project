# Generated by Django 4.0.2 on 2022-05-04 14:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Crop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(blank=True, max_length=60)),
                ('fieldcropid', models.CharField(blank=True, max_length=60)),
                ('croptype', models.CharField(blank=True, max_length=60)),
                ('cropvariety', models.CharField(blank=True, max_length=60)),
                ('name', models.CharField(blank=True, max_length=60)),
                ('expecyieldpeh', models.CharField(blank=True, max_length=60)),
                ('avgplanthei', models.CharField(blank=True, max_length=60)),
                ('expecperi', models.CharField(blank=True, max_length=60)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
