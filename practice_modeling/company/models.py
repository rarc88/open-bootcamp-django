from django.db import models


class Salary(models.Model):
    amount = models.FloatField(null=False, blank=False)
    extra_dec = models.BooleanField(default=False)
    extra_jan = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.amount


class Job(models.Model):
    title = models.CharField(max_length=15, blank=False, null=False)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return self.title

    # Relations
    salary = models.ForeignKey(Salary, on_delete=models.CASCADE)


class Country(models.Model):
    name = models.CharField(max_length=15, blank=False, null=False)
    country_code = models.CharField(max_length=6, blank=False, null=False)

    def __str__(self) -> str:
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self) -> str:
        return self.name

    # Relations
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class Place(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    address = models.CharField(max_length=50, blank=False, null=False)
    zip_code = models.CharField(max_length=5, blank=False, null=False)

    def __str__(self) -> str:
        return self.name

    # Relations
    location = models.ForeignKey(Location, on_delete=models.CASCADE)


class Employee(models.Model):
    id_number = models.CharField(max_length=10, blank=False, null=False)
    name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(max_length=30, blank=False, null=False)
    address = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self) -> str:
        return self.name

    # Relations
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
