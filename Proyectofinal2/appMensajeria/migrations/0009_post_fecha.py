# Generated by Django 4.0.6 on 2022-08-29 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMensajeria', '0008_remove_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='fecha',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]