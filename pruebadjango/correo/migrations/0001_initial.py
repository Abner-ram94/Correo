# Generated by Django 3.0.5 on 2020-07-07 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.CharField(max_length=25)),
                ('asunto', models.CharField(max_length=25)),
                ('mensaje', models.CharField(max_length=120)),
                ('adjuntar', models.CharField(max_length=120)),
            ],
        ),
    ]
