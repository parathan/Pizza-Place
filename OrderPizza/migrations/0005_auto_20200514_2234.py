# Generated by Django 3.0.6 on 2020-05-15 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrderPizza', '0004_subtoppings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasta',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='platters',
            name='largeprice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='platters',
            name='smallprice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='regular',
            name='largeprice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='regular',
            name='smallprice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='salads',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='sicilian',
            name='largeprice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='sicilian',
            name='smallprice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='subs',
            name='largeprice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='subs',
            name='smallprice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='subtoppings',
            name='largeprice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='subtoppings',
            name='smallprice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
    ]