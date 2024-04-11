from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Book(models.Model):
    title = models.CharField(verbose_name=_("Title"), max_length=100)
    author = models.CharField(verbose_name=_("Author"), max_length=100)
    description = models.TextField(verbose_name=_("Description"))
    best_seller = models.BooleanField(verbose_name=_("Best Seller"), default=False)
    age_group = models.CharField(verbose_name=_("Age Group"), max_length=50)
    category = models.CharField(verbose_name=_("Category"), max_length=50)
    price = models.DecimalField(verbose_name=_("Price"), max_digits=5, decimal_places=2)
    stock = models.IntegerField(verbose_name=_("Stock"))
    cover = models.ImageField(verbose_name=_("Cover"), upload_to='media/covers/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['best_seller', 'title']
        verbose_name = _("Book")
        verbose_name_plural = _("Books")


