from django.db import models

from core.models import CRMBase


class Boundary(CRMBase):
    """
    A boundary is an official political boundary, represented by a
    polygon-based geospatial record that can be associated
    with a variety of other spatial overlays, such as governing bodies and
    political subdivisions.
    """

    # TODO: Define "root" of reform effort area, such as the state, and use that
    # to generate the base map. Only one record can be the root!

    # For now, boundaries can only have one parent, which is almost always true
    parent = models.ForeignKey(
        'Boundary',
        null=True,
        blank=True,
        on_delete=models.PROTECT
    )
    # Name should be the official name of the jurisdiction
    name = models.CharField(
        max_length=255
    )
    # Defined areas based off of this: https://www2.census.gov/geo/pdfs/reference/geodiagram.pdf
    # The focus is on areas with jurisdiction over elections
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


class Region(CRMBase):
    """
    User-defined regions for use in organizations.
    """

    org_account = models.ForeignKey('accounts.OrganizationAccount', on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    boundaries = models.ManyToManyField(Boundary)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Regions'


class Site(CRMBase):
    """
    A Site is a point-based geospatial record.
    """

    name = models.CharField(
        max_length=255
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    # TODO: Add mailing address
    has_physical_address = models.BooleanField(
        default=False
    )
    physical_street_number = models.CharField(
        null=True,
        blank=True,
        max_length=10
    )
    physical_street_direction = models.CharField(null=True, blank=True, max_length=10)
    physical_street_name = models.CharField(null=True, blank=True, max_length=255)
    physical_street_suffix = models.CharField(null=True, blank=True, max_length=100)
    physical_unit_number = models.CharField(null=True, blank=True, max_length=50)
    physical_city = models.CharField(null=True, blank=True, max_length=255)
    physical_state = models.CharField(null=True, blank=True, max_length=255)
    physical_zip_code = models.CharField(null=True, blank=True, max_length=10)
    physical_county = models.CharField(null=True, blank=True, max_length=255)
    physical_latitude = models.FloatField(null=True, blank=True)
    physical_longitude = models.FloatField(null=True, blank=True)
    has_mailing_address = models.BooleanField(
        default=False
    )
    mailing_street_number = models.CharField(
        null=True,
        blank=True,
        max_length=10
    )
    mailing_street_direction = models.CharField(null=True, blank=True,
                                                 max_length=10)
    mailing_street_name = models.CharField(null=True, blank=True,
                                            max_length=255)
    mailing_street_suffix = models.CharField(null=True, blank=True,
                                              max_length=100)
    mailing_unit_number = models.CharField(null=True, blank=True,
                                            max_length=50)
    mailing_po_box = models.CharField(null=True, blank=True, max_length=255)
    mailing_city = models.CharField(null=True, blank=True, max_length=255)
    mailing_state = models.CharField(null=True, blank=True, max_length=255)
    mailing_zip_code = models.CharField(null=True, blank=True, max_length=10)
    mailing_county = models.CharField(null=True, blank=True, max_length=255)
    mailing_latitude = models.FloatField(null=True, blank=True)
    mailing_longitude = models.FloatField(null=True, blank=True)

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
        return ' '.join([i for i in parts if i is not None])

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
        return ' '.join([i for i in parts if i is not None])

    def physical_coordinates(self):
        return self.physical_latitude, self.physical_longitude

    def mailing_coordinates(self):
        return self.mailing_latitude, self.mailing_longitude

    def __str__(self):
        return self.name


class Location(CRMBase):
    """

    """

    parent = models.ForeignKey('Location', on_delete=models.PROTECT, blank=True, null=True)
    site = models.ForeignKey(Site, on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    unit = models.CharField(null=True, blank=True, max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name