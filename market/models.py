from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    author = models.CharField(max_length=100, verbose_name=_("Author"))
    description = models.TextField(verbose_name=_("Description"))
    best_seller = models.BooleanField(default=False, verbose_name=_("Best Seller"))
    age_group = models.CharField(max_length=50, verbose_name=_("Age Group"))
    category = models.CharField(max_length=50, verbose_name=_("Category"))
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Price"))
    stock = models.IntegerField(verbose_name=_("Stock"))
    media = models.ImageField(upload_to='media/', null=True, blank=True, verbose_name=_("Media"))

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['best_seller', 'title']
        verbose_name = _("Book")
        verbose_name_plural = _("Books")


