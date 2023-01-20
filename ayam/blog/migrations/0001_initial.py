# Generated by Django 4.1.3 on 2023-01-09 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kelas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kelas', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mata_kuliah', models.CharField(max_length=255)),
                ('dosen', models.CharField(max_length=255)),
                ('kelas', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.kelas')),
            ],
        ),
    ]
