# Generated by Django 5.1.4 on 2024-12-28 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20)),
                ('anio', models.IntegerField()),
                ('fecha', models.DateField()),
            ],
        ),
    ]
