# Generated by Django 4.1.3 on 2023-01-15 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_daftarmenu_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Karyawan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('jabatan', models.CharField(max_length=50)),
                ('gambar', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Pesanan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
