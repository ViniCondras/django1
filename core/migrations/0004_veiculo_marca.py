# Generated by Django 4.2.1 on 2023-06-27 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_veiculo'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='marca',
            field=models.CharField(default='sem marca', max_length=20, verbose_name='Marca'),
        ),
    ]
