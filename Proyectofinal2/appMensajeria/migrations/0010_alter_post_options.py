# Generated by Django 4.0.6 on 2022-08-29 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appMensajeria', '0009_post_fecha'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-id']},
        ),
    ]
