from django.db import models
from django.utils.translation import gettext as _
from market.choices import cover_types


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(verbose_name=_("First Name"), max_length=100)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=255)
    date_of_birth = models.DateField(verbose_name=_("Date of Birth"))
    date_of_death = models.DateField(verbose_name=_("Date of Death"), null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(verbose_name=_("Category Name"), max_length=50)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = _("Category Name")
        verbose_name_plural = _("Category Names")


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name=_("Author"), related_name='books')
    categories = models.ManyToManyField(Category, verbose_name=_("Categories"))
    title = models.CharField(verbose_name=_("Title"), max_length=100)
    description = models.TextField(verbose_name=_("Description"))
    best_seller = models.BooleanField(verbose_name=_("Best Seller"), default=False)
    age_group = models.CharField(verbose_name=_("Age Group"), max_length=50)
    price = models.DecimalField(verbose_name=_("Price"), max_digits=5, decimal_places=2)
    stock = models.IntegerField(verbose_name=_("Stock"))
    cover_type = models.CharField(verbose_name=_("Cover Type"), choices=cover_types, max_length=30,
                                  default="soft", null=True)
    cover = models.ImageField(verbose_name=_("Cover"), upload_to='covers/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['best_seller', 'title']
        verbose_name = _("Book")
        verbose_name_plural = _("Books")
