from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.




class Product(models.Model):
    PROname = models.CharField(max_length=100, verbose_name=_("Product name"))
    PROcategory =models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("Category"))
    PRObrand = models.ForeignKey('settings.Brand', on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("Product Brand"))
    PROdesc = models.TextField(verbose_name=_("Product description"))
    PROimage = models.ImageField(upload_to='product/primary/', verbose_name=_("Image"), blank=True, null=True)
    PROprice = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Price"))
    PROdisprice = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Discount Price"))
    PROcost = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Cost"))
    PROcreated = models.DateTimeField(verbose_name=_("Created at"))

    PROslug = models.SlugField(blank=True, null=True, verbose_name=_("Slug"))
    PROnew = models.BooleanField(default=True, verbose_name=_("NEW"))
    PRObestsaler = models.BooleanField(default=False, verbose_name=_("Best Saler"))


    def save(self, *args, **kwargs):
        if not self.PROslug :
            self.PROslug = slugify(self.PROname )
        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def get_absolute_url(self):
        return reverse("products:product_detail", kwargs={"slug": self.PROslug})
               

    def __str__(self):
        return self.PROname


class ProductImage(models.Model):
    PRDIproduct = models.ForeignKey(Product,on_delete=models.CASCADE, verbose_name=_("Product"))
    PRDIimage = models.ImageField(upload_to='product/', verbose_name=_("Image"))
    

    def __str__(self):
        return str(self.PRDIproduct)


class Category(models.Model):
    CATname = models.CharField(max_length=50, verbose_name=_("Category name"))
    CATparent = models.ForeignKey('self', limit_choices_to={'CATparent__isnull' : True},on_delete=models.CASCADE, blank=True, null=True, verbose_name=_("Category parent"))
    CATdesc = models.TextField(verbose_name=_("Category description"))
    CATimg = models.ImageField(upload_to='category/', verbose_name=_("Category image"))
    CATslug = models.SlugField(blank=True, null=True, verbose_name=_("Category slug"))


    def save(self, *args, **kwargs):
        if not self.CATslug :
           self.CATslug = slugify(self.CATname )
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


    def get_absolute_url(self):
        return reverse("products:cat_detail", kwargs={"slug": self.CATslug})        

    def __str__(self):
        return self.CATname


class Product_Alternative(models.Model):
    PALNproduct = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='main_product_Alt', verbose_name=_("Product"))
    PALNalternative = models.ManyToManyField(Product, related_name='product_alternative', verbose_name=_("Alternatives"))

    class Meta:
        verbose_name = _("Product Alternative")
        verbose_name_plural = _("Product Alternatives")

    def __str__(self):
        return str(self.PALNproduct)


class Product_Accessories(models.Model):
    PACCproduct = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='main_product_Acc', verbose_name=_("Product"))
    PACCalternative = models.ManyToManyField(Product, related_name='product_Accessories', verbose_name=_("Accessories"))

    class Meta:
        verbose_name = _("Product Accessory")
        verbose_name_plural = _("Product Accessories")                           