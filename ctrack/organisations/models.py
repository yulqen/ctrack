from django.db import models

from django.contrib.auth import get_user_model

from django.urls import reverse
from django.conf import settings
from django_extensions.db.fields import AutoSlugField
from slugify import slugify


class AddressType(models.Model):
    descriptor = models.CharField(max_length=50)

    def __str__(self):
        return self.descriptor


class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=255)
    organisation = models.ForeignKey("Organisation", on_delete=models.CASCADE)
    role = models.ManyToManyField(Role)
    email = models.EmailField()
    mobile = models.CharField(max_length=20, blank=True)
    landline = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name

    def get_organisation_name(self):
        return self.organisation.name

    class Meta:
        verbose_name_plural = "People"


class Mode(models.Model):
    descriptor = models.CharField(max_length=100)

    def __str__(self):
        return self.descriptor


class Submode(models.Model):
    descriptor = models.CharField(max_length=100)
    mode = models.ForeignKey(Mode, on_delete=models.CASCADE)

    def __str__(self):
        return self.descriptor


class Organisation(models.Model):

    DESIGNATION_TYPE = [
        (1, "Automatic"),
        (2, "Reserve Power"),
    ]

    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from=["name"])
    submode = models.ForeignKey(
        Submode, on_delete=models.CASCADE, blank=True, null=True
    )
    designation_type = models.IntegerField(choices=DESIGNATION_TYPE, default=1)
    registered_company_name = models.CharField(max_length=255, blank=True)
    registered_company_number = models.CharField(max_length=100, blank=True)
    date_updated = models.DateField(auto_now=True)
    updated_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    comments = models.TextField(max_length=500)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("organisations:detail", kwargs={"slug": self.slug})

    def slugify_name(self):
        return slugify(self.name)

    def __str__(self):
        return self.name


class Address(models.Model):
    organisation = models.ForeignKey(
        Organisation, related_name="addresses", on_delete=models.CASCADE, blank=False
    )
    type = models.ForeignKey(
        AddressType, verbose_name="Address Type", on_delete=models.CASCADE, blank=False
    )
    line1 = models.CharField(max_length=255)
    line2 = models.CharField(max_length=255, blank=True)
    line3 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    county = models.CharField(max_length=100, blank=True)
    postcode = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    other_details = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return " ".join([self.organisation.name, self.line1])

    class Meta:
        verbose_name_plural = "Addresses"
