# Generated by Django 3.0.6 on 2020-05-15 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrderPizza', '0003_auto_20200514_2114'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubToppings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('smallprice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('largeprice', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'SubToppings',
            },
        ),
    ]
