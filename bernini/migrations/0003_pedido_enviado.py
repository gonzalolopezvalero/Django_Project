# Generated by Django 2.2.16 on 2020-11-02 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bernini', '0002_auto_20201101_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='enviado',
            field=models.BooleanField(default=False, verbose_name='Enviado'),
        ),
    ]