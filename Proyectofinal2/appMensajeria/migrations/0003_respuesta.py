# Generated by Django 4.0.6 on 2022-08-28 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMensajeria', '0002_post_email_post_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mecanico', models.CharField(max_length=50)),
                ('respuesta', models.TextField()),
            ],
        ),
    ]
