from uuid import uuid4
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import django.utils.timezone

current_year = django.utils.timezone.now().year
min_year = current_year - 70


class Car(models.Model):
    id = models.UUIDField(default=uuid4, unique=True,
                          primary_key=True, editable=False)
    mark = models.CharField(max_length=100, null=True, blank=False)
    model = models.CharField(max_length=50, null=True, blank=False)
    generation = models.CharField(max_length=50, null=True, blank=False)
    begin_production = models.IntegerField(null=True, blank=False, validators=[
                                           MinValueValidator(min_year), MaxValueValidator(current_year)])
    end_production = models.IntegerField(null=True, blank=True, validators=[
                                         MinValueValidator(min_year), MaxValueValidator(current_year)])

    def __str__(self):
        if self.end_production == None:
            self.end_production = ''

        return f'{self.model} {self.generation} Produkcja: {self.begin_production}-{self.end_production}'

    def get_models(selected_mark):
        return Car.objects.filter(mark=selected_mark)

    def get_engines(selected_model):
        return Car.objects.filter(model=selected_model)


class Vendor(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, unique=True)
    name = models.CharField(max_length=50, null=True, blank=False)
    address = models.CharField(max_length=100, null=True, blank=False)

    def __str__(self):
        return f'{self.name}'


class Engine(models.Model):
    FUEL_TYPES = (
        ('d', 'Diesel Engine'),
        ('g', 'Gas Engine')
    )

    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    car_id = models.ForeignKey(Car, on_delete=models.DO_NOTHING)
    engine_code = models.CharField(max_length=50, null=True, blank=False)
    capacity = models.IntegerField(null=True, blank=False)
    power = models.IntegerField(null=True, blank=False)
    fuel_type = models.CharField(max_length=1, null=True, choices=FUEL_TYPES)
    begin_production = models.IntegerField(null=True, blank=False, validators=[
                                           MinValueValidator(min_year), MaxValueValidator(current_year)])
    end_production = models.IntegerField(null=True, blank=False, validators=[
                                         MinValueValidator(min_year), MaxValueValidator(current_year)])

    def __str__(self):
        return f'{self.car_id.mark} / {self.engine_code} / {self.begin_production}-{self.end_production} / {self.capacity}cm3'


class Part(models.Model):
    id = models.UUIDField(default=uuid4, unique=True,
                          primary_key=True)

    engine_id = models.ForeignKey(Engine, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    catalog_number = models.CharField(max_length=75, null=True, blank=False)
    name = models.CharField(max_length=255, null=True, blank=False)
    description = models.TextField(max_length=5000, null=True, blank=True)
    quality_fac = models.FloatField(null=False, blank=False, validators=[
                                    MinValueValidator(1), MaxValueValidator(100)])
    price = models.FloatField(default=0, null=True, blank=False)
    time_of_delivery = models.IntegerField(null=False, blank=False, validators=[
                                           MinValueValidator(1), MaxValueValidator(60)])
    quantity = models.IntegerField(null=True, blank=False)
    is_original = models.BooleanField(null=True, blank=False)
    original_id = models.ForeignKey(
        "self", on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        if self.is_original == False:
            return f'{self.name}'
        return self.name

    # All 4 functions to get the best quality, the cheapest price, the fastest delivery and weighted average of all coefficients
    def lowest_price(parts):

        lowest_price_part = parts[0]
        for part in parts:
            if part.price < lowest_price_part:
                lowest_price_part = part.price

        return lowest_price_part

    def part_sum(self, quality, price, time):
        return round((0.5 * self.quality_fac) - (0.35 * self.price) - (0.15 * self.time_of_delivery), 2)

    # Correction after save new product
    def save(self, *args, **kwargs):

        # Price of any part in shop cannot be equal 0
        if self.price <= 0:
            self.price = 10

        # If part is original, for logical schema this part don't have parent then set this param as NULL, and round price to second decimal place
        self.price = round(self.price, 2)

        super(Part, self).save(*args, **kwargs)
