# Generated by Django 2.2.1 on 2019-05-12 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20190505_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotsale',
            name='dia_inicial',
            field=models.DateField(help_text='Fecha de inicio de la semana. Debe tener al menos 7 días de diferencia con la de otra semana.'),
        ),
        migrations.AlterField(
            model_name='subasta',
            name='dia_inicial',
            field=models.DateField(help_text='Fecha de inicio de la semana. Debe tener al menos 7 días de diferencia con la de otra semana.'),
        ),
    ]
