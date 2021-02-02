from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
import datetime
from django_countries.fields import CountryField
from django.utils.text import slugify
from django.db.models.signals import post_save
# Create your models here.




class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_img', verbose_name=_("Image"), blank=True, null=True)
    addres = models.CharField(max_length=100, verbose_name=_("Address"))
    join_date = models.DateTimeField(default=datetime.datetime.now, verbose_name=_("join date"))
    country = CountryField() 
    slug = models.SlugField(blank=True, null=True, verbose_name=_("Slug"))
    

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)        

    def __str__(self):
        return '%s' %(self.user)

    def get_absolute_url(self):
        return reverse("accounts:profile", kwargs={"slug": self.slug})

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = Profile.objects.create(user=kwargs['instance'])

    post_save.connect(create_profile, sender= User)            

