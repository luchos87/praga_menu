# Generated by Django 3.2.8 on 2022-05-03 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=300)),
                ('fecha_nac', models.DateField()),
            ],
        ),
    ]
