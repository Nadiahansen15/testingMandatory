# Generated by Django 3.2 on 2021-10-25 08:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cellphone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='keaNet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InternetConnection', models.BooleanField()),
                ('PhoneLines', models.IntegerField(validators=[django.core.validators.MaxValueValidator(8)])),
                ('totalPrice', models.FloatField()),
                ('cellphone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cellphone.cellphone')),
            ],
        ),
    ]
