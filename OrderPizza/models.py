from django.db import models

# Create your models here.
class Regular(models.Model):
    type = models.CharField(max_length=50)
    smallprice = models.DecimalField(max_digits = 10, decimal_places=2, blank=True)
    largeprice = models.DecimalField(max_digits = 10, decimal_places=2, blank=True)
    class Meta:
        verbose_name_plural = "Regular"

class Sicilian(models.Model):
    type = models.CharField(max_length=50)
    smallprice = models.DecimalField(max_digits = 10, decimal_places=2, blank=True)
    largeprice = models.DecimalField(max_digits = 10, decimal_places=2, blank=True)
    class Meta:
        verbose_name_plural = "Sicilian"

class Toppings(models.Model):
    topping = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "Toppings"

class Subs(models.Model):
    type = models.CharField(max_length=50)
    smallprice = models.DecimalField(max_digits = 10, decimal_places=2, blank=True, null=True)
    largeprice = models.DecimalField(max_digits = 10, decimal_places=2, blank=True, null=True)
    class Meta:
        verbose_name_plural = "Subs"

class SubToppings(models.Model):
    type = models.CharField(max_length=50)
    smallprice = models.DecimalField(max_digits = 10, decimal_places = 2, blank=True, null=True)
    largeprice = models.DecimalField(max_digits = 10, decimal_places = 2, blank=True, null=True)
    class Meta:
        verbose_name_plural = "SubToppings"

class Pasta(models.Model):
    type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits = 10, decimal_places=2, blank=True, null=True)
    class Meta:
        verbose_name_plural = "Pasta"

class Salads(models.Model):
    type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits = 10, decimal_places=2, blank=True, null=True)
    class Meta:
        verbose_name_plural = "Salads"

class Platters(models.Model):
    type = models.CharField(max_length=50)
    smallprice = models.DecimalField(max_digits = 10, decimal_places=2, blank=True, null=True)
    largeprice = models.DecimalField(max_digits = 10, decimal_places=2, blank=True, null=True)
    class Meta:
        verbose_name_plural = "Platters"
