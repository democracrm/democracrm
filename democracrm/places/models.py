from django.contrib.gis.db import models

from core.models import CRMBase, CRMTreeBase


class Boundary(CRMTreeBase):
    """
    A boundary is an official political boundary, represented by a
    polygon-based geospatial record that can be associated
    with a variety of other spatial overlays, such as governing bodies and
    political subdivisions.
    """

    # For now, boundaries can only have one parent, which is almost always true

    # Name should be the official name of the jurisdiction
    name = models.CharField(
        max_length=255
    )
    description = models.TextField(blank=True)
    # Defined areas based off of this: https://www2.census.gov/geo/pdfs/reference/geodiagram.pdf
    # The focus is on areas with jurisdiction over legislation and elections
    # The boundaries will be considered surrounding or within whatever level is defined
    LEVEL_CHOICES = (
        ('nation', 'Nation'),
        ('state', 'State'),
        ('county', 'County'),
        ('municipality', 'Municipality'),
    )
    level = models.CharField(
        max_length=255,
        choices=LEVEL_CHOICES,
    )

    class Meta:
        verbose_name_plural = "Boundaries"

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class RegionGroup(CRMBase):
    """
    Group of Region objects in a one-to-many topology.
    """

    # TODO: Should it be hierarchical?

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    overlapping_enabled = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Region Groups'

    def __str__(self):
        return self.name


class Region(CRMBase):
    """
    User-defined regions for use in organizations.
    """

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    boundaries = models.ManyToManyField(Boundary, blank=True)
    group = models.ForeignKey(RegionGroup, blank=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Regions'

    def __str__(self):
        return self.name


class SiteGroup(CRMBase):
    """
    Group of Site objects in a one-to-many topology.
    """

    # TODO: Should it be hierarchical?

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Site Groups'

    def __str__(self):
        return self.name


class Site(CRMBase):
    """
    A Site is a point-based geospatial record.
    """

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    group = models.ForeignKey(SiteGroup, blank=True, null=True,
                              on_delete=models.PROTECT)
    # TODO: Add mailing address
    has_physical_address = models.BooleanField(
        default=False
    )
    physical_street_number = models.CharField(
        blank=True,
        max_length=10
    )
    physical_street_direction = models.CharField(blank=True, max_length=10)
    physical_street_name = models.CharField(blank=True, max_length=255)
    physical_street_suffix = models.CharField(blank=True, max_length=100)
    physical_unit_number = models.CharField(blank=True, max_length=50)
    physical_city = models.CharField(blank=True, max_length=255)
    physical_state = models.CharField(blank=True, max_length=255)
    physical_zip_code = models.CharField(blank=True, max_length=10)
    physical_county = models.CharField(blank=True, max_length=255)
    physical_latitude = models.FloatField(null=True, blank=True)
    physical_longitude = models.FloatField(null=True, blank=True)
    has_mailing_address = models.BooleanField(
        default=False
    )
    mailing_street_number = models.CharField(
        blank=True,
        max_length=10
    )
    mailing_street_direction = models.CharField(blank=True, max_length=10)
    mailing_street_name = models.CharField(blank=True, max_length=255)
    mailing_street_suffix = models.CharField(blank=True, max_length=100)
    mailing_unit_number = models.CharField(blank=True, max_length=50)
    mailing_po_box = models.CharField(blank=True, max_length=255)
    mailing_city = models.CharField(blank=True, max_length=255)
    mailing_state = models.CharField(blank=True, max_length=255)
    mailing_zip_code = models.CharField(blank=True, max_length=10)
    mailing_county = models.CharField(blank=True, max_length=255)
    mailing_latitude = models.FloatField(null=True, blank=True)
    mailing_longitude = models.FloatField(null=True, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Sites'

    def __str__(self):
        return self.name

    def full_physical_address(self):
        parts = []
        parts.append(self.physical_street_number)
        parts.append(self.physical_street_direction)
        parts.append(self.physical_street_name)
        parts.append(self.physical_street_suffix)
        parts.append(self.physical_unit_number)
        parts.append(self.physical_city)
        parts.append(self.physical_state)
        parts.append(self.physical_zip_code)
        return ' '.join([i for i in parts if i])

    def full_mailing_address(self):
        parts = []
        parts.append(self.mailing_street_number)
        parts.append(self.mailing_street_direction)
        parts.append(self.mailing_street_name)
        parts.append(self.mailing_street_suffix)
        parts.append(self.mailing_unit_number)
        parts.append(self.mailing_po_box)
        parts.append(self.mailing_city)
        parts.append(self.mailing_state)
        parts.append(self.mailing_zip_code)
        return ' '.join([i for i in parts if i])

    def physical_coordinates(self):
        return self.physical_latitude, self.physical_longitude

    def mailing_coordinates(self):
        return self.mailing_latitude, self.mailing_longitude


class Location(CRMTreeBase):
    """

    """

    site = models.ForeignKey(Site, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    unit = models.CharField(blank=True, max_length=255)

    class Meta:
        verbose_name_plural = 'Locations'

    def __str__(self):
        return self.name
