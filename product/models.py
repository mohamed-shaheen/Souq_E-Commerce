from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.




class Product(models.Model):
    PROName = models.CharField(max_length=100, verbose_name=_("Product name"))
    #PROCategory =
    PRODesc = models.TextField(verbose_name=_("Product description"))
    PROPrice = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Price"))
    PROCost = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Cost"))
    PROCreated = models.DateTimeField(verbose_name=_("Created at"))

    def __str__(self):
        return self.PROName


class ProductImage(models.Model):
    PRDIProduct = models.ForeignKey(Product,on_delete=models.CASCADE, verbose_name=_("Product"))
    PRDIImage = models.ImageField(upload_to='product/', verbose_name=_("Image"))
    

    def __str__(self):
        return str(self.PRDIProduct)

