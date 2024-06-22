# Generated by Django 4.2.1 on 2023-07-27 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portafolio', '0011_alter_projecto_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presentacion',
            fields=[
                ('image', models.ImageField(upload_to='Portafolio/images/')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
