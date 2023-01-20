# Generated by Django 4.1.3 on 2023-01-15 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_gambar_alter_post_harga'),
    ]

    operations = [
        migrations.CreateModel(
            name='DaftarMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('makanan', models.CharField(max_length=255, null=True)),
                ('harga', models.DecimalField(decimal_places=0, max_digits=6)),
                ('gambar', models.ImageField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]