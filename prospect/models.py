from django.conf import settings
from django.db import models

from localflavor.us.models import USPostalCodeField


class Prospect(models.Model):

    """A prospective customer contact and all related information about them."""

    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=64, null=True, blank=True)
    last_name = models.CharField(max_length=64, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = USPostalCodeField(null=True, blank=True)
    zipcode = models.CharField(max_length=10, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    company = models.ForeignKey('Company', null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name,)

    class Meta:
        verbose_name = 'Prospect'
        verbose_name_plural = 'Prospects'


class Company(models.Model):

    """A company profile that prospects are associated with. """

    name = models.CharField(max_length=64)

    def __str__(self):
        return "{}".format(self.name,)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class ProspectNote(models.Model):

    """Notes for a given prospect."""

    prospect = models.ForeignKey(Prospect, on_delete=models.CASCADE)
    notes = models.TextField(blank=True)

    def __str__(self):
        return "{} {}".format(self.prospect.first_name, self.prospect.last_name)

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'


class ProspectList(models.Model):

    """A list of prospects."""

    name = models.CharField(max_length=64)
    prospects = models.ManyToManyField('Prospect', blank=True, related_name='lists')

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name = 'Prospect List'
        verbose_name_plural = 'Prospect Lists'
