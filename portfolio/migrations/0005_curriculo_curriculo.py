# Generated by Django 3.0.6 on 2020-05-15 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_curriculo'),
    ]

    operations = [
        migrations.AddField(
            model_name='curriculo',
            name='curriculo',
            field=models.BinaryField(blank=True, verbose_name='curriculo'),
        ),
    ]
