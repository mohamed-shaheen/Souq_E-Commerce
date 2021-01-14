from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Brand(models.Model):

    BRname = models.CharField(max_length=40, verbose_name=_("Brand name"))
    BRdesc = models.TextField(blank=True, null=True, verbose_name=_("Brand description"))

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self):
        return self.BRname


class Variant(models.Model):
    
    VARname = models.CharField(max_length=40)
    VARdesc = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = _("Variant")
        verbose_name_plural = _("Variants")

    def __str__(self):
        return self.VARname